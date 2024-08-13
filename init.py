from app import create_app
from flask_security import hash_password
from werkzeug.security import generate_password_hash
from database.models import db, user_datastore
from app import app

import subprocess

from database.models import *

with app.app_context():
    # Drop all tables
    db.drop_all()
    
    # Create all tables
    db.create_all()

    # Create roles
    admin_role = Role(name='admin', description='Administrator')
    sponsor_role = Role(name='sponsor', description='Sponsor')
    influencer_role = Role(name='influencer', description='Influencer')
    db.session.add(admin_role)
    db.session.add(sponsor_role)
    db.session.add(influencer_role)
    db.session.commit()

    # Create admin user
    admin_user = user_datastore.create_user(
        email='admin@adfluence.com',
        username='admin',
        password=hash_password('password'),
        roles=[admin_role]
    )
    db.session.commit()

    # # Create sponsor user
    # sponsor_user = user_datastore.create_user(
    #     email='sponsor@adfluence.com',
    #     username='santosh',
    #     password=hash_password('password'),
    #     roles=[sponsor_role]
    # )

    # # Create influencer user
    # influencer_user = user_datastore.create_user(
    #     email='influencer@adfluence.com',
    #     username='ashish',
    #     password=hash_password('password'),
    #     roles=[influencer_role]
    # )

    # db.session.commit()

    #  # Create a sponsor profile
    # sponsor_profile = Sponsor(
    #     company_name='Company Name',
    #     industry='Industry',
    #     budget=10000,
    #     user_id=sponsor_user.id
    # )
    # db.session.add(sponsor_profile)
    # db.session.commit()

    # # Create an influencer profile
    # influencer_profile = Influencer(
    #     category='Category',
    #     niche='Niche',
    #     reach=5000,
    #     user_id=influencer_user.id
    # )
    # db.session.add(influencer_profile)
    # db.session.commit()
    
    # # Create a campaign
    # campaign = Campaign(
    #     name='Campaign 1',
    #     sponsor_id=sponsor_profile.sponsor_id,
    #     description='Campaign Description',
    #     status=False,
    #     start_date=datetime(2024, 1, 1),
    #     end_date=datetime(2024, 6, 1),
    #     updated_at=datetime.utcnow(),
    #     campaign_img='campaign1.jpg',
    #     budget=5000,
    #     visibility='Public',
    #     goals='Goal 1',
    #     delete=False
    # )
    # db.session.add(campaign)
    # db.session.commit()

    # # Create an ad
    # ad = Ad(
    #     name='Ad 1',
    #     content='Ad Content',
    #     campaign_id=campaign.id,
    #     sponsor_id=sponsor_profile.sponsor_id,
    #     start_date=datetime(2024, 1, 10),
    #     requirements='Requirement 1',
    #     budget=1000,
    #     img='ad1.jpg',
    #     status=True,
    #     updated_at=datetime.utcnow(),
    #     target_audience='Audience 1',
    #     delete=False
    # )
    # db.session.add(ad)
    # db.session.commit()

    # # Create an ad request
    # ad_request = AdRequest(
    #     ad_id=ad.id,
    #     sponsor_id=sponsor_profile.sponsor_id,
    #     influencer_id=influencer_profile.influencer_id,
    #     campaign_id=campaign.id,
    #     message='Ad Request Message',
    #     status='Pending',
    #     request_date=datetime.utcnow(),
    #     requirements='Requirement 1',
    #     payment=500
    # )
    # db.session.add(ad_request)
    # db.session.commit()


    print("Database initialized with dummy data")
    # Run generate_tokens.py after everything is done
    subprocess.run(["python", "generate_tokens.py"])

    