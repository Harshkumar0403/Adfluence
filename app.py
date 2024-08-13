from flask import Flask, jsonify, request
from celery.schedules import crontab
from flask_security import verify_password
from flask_restful import Api
from flask_security import Security
from config import LocalDev
import sqlite3
from caching import cache
from database.models import db, user_datastore
from routes.security import security
from flask_cors import CORS
from worker import celery_init_app
from task import send_daily_reminders ,send_new_campaign_notifications, send_ad_request_notifications,send_ad_acceptance_notifications,send_monthly_report
from flask import Flask, request, jsonify



def create_app():
    app = Flask(__name__)
    app.config.from_object(LocalDev)
    db.init_app(app)
    api = Api(app)
    cache.init_app(app)
    security.init_app(app, user_datastore)
    CORS(app)
    with app.app_context():
        import routes.views

    return app,api,cache

app ,api,cache = create_app()
celery_app = celery_init_app(app)

from routes.auth import  login, register
api.add_resource(login, '/api/login')
api.add_resource(register, '/api/register')

from routes.campaign import CampaignResource, CampaignSpecific,CampaignUpdate
api.add_resource(CampaignResource, '/api/campaign')
api.add_resource(CampaignSpecific, '/api/campaign/<int:id>')
api.add_resource(CampaignUpdate, '/api/campaignUpdate/<int:id>')

from routes.ad import AdResource, AdSpecific
api.add_resource(AdResource, '/api/Ad')
api.add_resource(AdSpecific, '/api/Ad/<int:id>')

from routes.admin import CampaignDelete,AdDelete, toggle_user_status, UserResources ,exportCSV, InfluencerResources,SponsorResources,InfluencerSpecificResources,SponsorSpecificResources, UserSpecificResources
api.add_resource(CampaignDelete, '/api/category_delete/<int:id>')
api.add_resource(AdDelete, '/api/Ad_delete/<int:id>')
api.add_resource(toggle_user_status, '/api/toggle_user_status/<int:id>')
api.add_resource(UserResources, '/api/users')
api.add_resource(InfluencerResources, '/api/influencers')
api.add_resource(SponsorResources, '/api/sponsors')
api.add_resource(InfluencerSpecificResources, '/api/influencer/<int:id>')
api.add_resource(SponsorSpecificResources, '/api/sponsor/<int:id>')
api.add_resource( UserSpecificResources, '/api/user/<int:id>')
api.add_resource(exportCSV , '/api/export-csv')

from routes.adrequest import AdRequestResource , AdRequestStatusResource
api.add_resource(AdRequestResource, '/api/ad_request')
api.add_resource(AdRequestStatusResource , '/api/ad_request/<int:id>')


@celery_app.on_after_configure.connect
def automated_tasks(sender, **kwargs):
    # daily at 6 30
    sender.add_periodic_task(
        # 60,
        crontab(hour=16, minute=1 ,day_of_month=1),
        send_monthly_report.delay(),
    )
    sender.add_periodic_task(
        # 30,
        # crontab(hour=19,minute=58),
        send_daily_reminders.delay(),
    )
    sender.add_periodic_task(
        # 60,
        # crontab(hour=11, minute=30),
        send_new_campaign_notifications.delay(),
    )
    sender.add_periodic_task(
        60,
        crontab(hour=16, minute=1),
        send_ad_request_notifications.s(),
    )
    sender.add_periodic_task(
        60,
        crontab(hour=16, minute=1),
        send_ad_acceptance_notifications.s(),
    )
    





if __name__ == '__main__':
    app.run(debug=True)