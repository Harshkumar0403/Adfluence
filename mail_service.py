import logging
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email import encoders

SMTP_HOST = "localhost"
SMTP_PORT = 1025
SENDER_EMAIL = 'donot-reply@support.adfluence.com'
SENDER_PASSWORD = ''



def send_message(to, subject, content_body, attachment=None, filename=None):
    msg = MIMEMultipart()
    msg["To"] = to
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg.attach(MIMEText(content_body, 'html'))

    if attachment and filename:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment)
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment', filename=filename)
        msg.attach(part)

    client = SMTP(host=SMTP_HOST, port=SMTP_PORT)
    client.send_message(msg=msg)
    logging.debug("Email sent successfully.")
    client.quit()