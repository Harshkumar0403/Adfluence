from datetime import datetime, timedelta
import os
from io import StringIO
from io import StringIO, BytesIO
import csv
from flask import send_file
from celery import shared_task
from mail_service import send_message
from jinja2 import Template
from celery.utils.log import get_task_logger
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sqlite3
from jinja2 import Environment, FileSystemLoader,Template
from datetime import datetime

logger = get_task_logger(__name__)


env = Environment(loader=FileSystemLoader('.'))

def render_template(template_name, context):
    template = env.get_template(template_name)
    return template.render(context)

def fetch_data(query):
    conn = sqlite3.connect('instance/database.sqlite3')
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    return data


@shared_task(ignore_result=True)
def send_daily_reminders():
    users_query = """
    SELECT email, username FROM user
    WHERE  login_count IS NULL OR last_login_at < date('now', '-1 day')
    """
    users = fetch_data(users_query)
    for email, username in users:
        subject = "Reminder: Please visit Adfluence"
        context = {
            'name': username,
            'message': 'You have pending ad requests or haven\'t visited recently. Please log in to check them.'
        }
        content_body = render_template('email.html', context)
        send_message(email, subject, content_body)

@shared_task(ignore_result=True)
def send_new_campaign_notifications():
    query = "SELECT campaign_name, description FROM campaign WHERE created_at >= date('now', '-1 day')"
    campaigns = fetch_data(query)
    
    if campaigns:
        influencers_query = "SELECT u.email, u.username FROM user u JOIN influencer i ON u.user_id = i.user_id"
        influencers = fetch_data(influencers_query)
        
        for email, influencer_name in influencers:
            for campaign_name, description in campaigns:
                subject = f"New Campaign Added: {campaign_name}"
                context = {
                    'name': influencer_name,
                    'message': f'A new campaign "{campaign_name}" has been added.\n Description: {description}'
                }
                content_body = render_template('email.html', context)
                send_message(email, subject, content_body)

@shared_task(ignore_result=True)
def send_ad_request_notifications():
    ad_requests_query = """
    SELECT ar.ad_id, ad.name, u.email, u.username
    FROM ad_request ar
    JOIN ad ON ar.ad_id = ad.id
    JOIN influencer i ON ar.influencer_id = i.influencer_id
    JOIN user u ON i.user_id = u.id
    WHERE ar.status = 'pending'
    """
    ad_requests = fetch_data(ad_requests_query)
    
    for ad_id, ad_name, email, username in ad_requests:
        subject = f"New Ad Request: {ad_name}"
        context = {
            'name': username,
            'message': f'You have a new ad request opportunity for "{ad_name}". Please check Adfluence for further details.'
        }
        content_body = render_template('email.html', context)
        send_message(email, subject, content_body)

@shared_task(ignore_result=True)
def send_ad_acceptance_notifications():
    accepted_requests_query = """
    SELECT ar.ad_id, ad.name, u.email, u.username
    FROM ad_request ar
    JOIN ad ON ar.ad_id = ad.id
    JOIN sponsor s ON ar.sponsor_id = s.sponsor_id
    JOIN user u ON s.user_id = u.id
    WHERE ar.status = 'accepted'
    """
    accepted_requests = fetch_data(accepted_requests_query)
    
    for ad_id, ad_name, email, name in accepted_requests:
        subject = f"Ad Request Accepted: {ad_name}"
        context = {
            'name': name,
            'message': f'The ad request for "{ad_name}" has been accepted by an influencer. Please check Adfluence for further details.'
        }
        content_body = render_template('email.html', context)
        send_message(email, subject, content_body)


@shared_task(ignore_result=True)
def send_monthly_report():
    thirty_days_ago = datetime.now() - timedelta(days=30)

    report_query = f"""
    SELECT u.username AS sponsor_name,s.sponsor_id, c.name, COUNT(a.id) AS ads_done, COUNT(ar.id) AS ad_requests_sent
    FROM sponsor s
    JOIN user u ON s.user_id = u.id
    LEFT JOIN campaign c ON s.sponsor_id = c.sponsor_id
    LEFT JOIN ad a ON c.id = a.campaign_id AND a.start_date > '{thirty_days_ago}'
    LEFT JOIN ad_request ar ON s.sponsor_id = ar.sponsor_id AND ar.request_date > '{thirty_days_ago}' 
    GROUP BY s.sponsor_id, c.id
    """
    reports = fetch_data(report_query)

    for report in reports:
        sponsor_name,sponsor_id, campaign_name, ads_done, ad_requests_sent = report
        email_query = f"SELECT email FROM user WHERE id = (SELECT user_id FROM sponsor WHERE sponsor_id = '{sponsor_id}')"
        sponsor_email = fetch_data(email_query)[0][0]

        subject = "Monthly Activity Report"
        context = {
            'sponsor_name': sponsor_name,
            'campaign_name': campaign_name,
            'ads_done': ads_done,
            'ad_requests_sent': ad_requests_sent,
            'month': thirty_days_ago.strftime("%B %Y")
        }
        content_body = render_template('monthly_report.html', context)
        send_message(sponsor_email, subject, content_body)


def generate_csv_report(sponsor_id, sponsor_email):
    query = f"""
    SELECT c.name, c.description, c.start_date, c.end_date, c.budget, c.visibility, c.goals
    FROM campaign c
    WHERE c.sponsor_id = {sponsor_id}
    """
    campaigns = fetch_data(query)

    # Create CSV
    csv_output = StringIO()
    writer = csv.writer(csv_output)
    writer.writerow(['Campaign Name', 'Description', 'Start Date', 'End Date', 'Budget', 'Visibility', 'Goals'])

    for campaign in campaigns:
        writer.writerow(campaign)

    csv_content = csv_output.getvalue().encode('utf-8')
    csv_output.close()


    send_file(csv_content, mimetype='text/csv', download_name='campaigns_report.csv', as_attachment=True)
    # Send email
    subject = "Your Campaign Report is Ready"
    content_body = f"""
    <p>Hi,</p>
    <p>Your campaign report is ready. You can download it from the attachment.</p>
    <p>Regards,<br>Support Adfluence</p>
    """
    send_message(to=sponsor_email, subject=subject, content_body=content_body, attachment=csv_content, filename='campaigns_report.csv')
    
    print("done till last")
