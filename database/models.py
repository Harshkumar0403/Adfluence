from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.mutable import MutableList
from datetime import datetime
from flask_security import UserMixin, RoleMixin, AsaList, SQLAlchemyUserDatastore

db = SQLAlchemy()

roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
)

class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    last_login_at = db.Column(db.DateTime)
    current_login_at = db.Column(db.DateTime)
    last_login_ip = db.Column(db.String(255))
    current_login_ip = db.Column(db.String(255))
    login_count = db.Column(db.Integer)
    active = db.Column(db.Boolean)
    fs_uniquifier = db.Column(db.String(255), unique=True)
    confirmed_at = db.Column(db.DateTime)
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'username': self.username,
            'last_login_at': self.last_login_at,
            'current_login_at': self.current_login_at,
            'last_login_ip': self.last_login_ip,
            'current_login_ip': self.current_login_ip,
            'login_count': self.login_count,
            'active': self.active,
            'fs_uniquifier': self.fs_uniquifier,
            'confirmed_at': self.confirmed_at,
            'roles': [role.name for role in self.roles]
        }

    @staticmethod
    def get_all_users():
        return User.query.all()
    

class Sponsor(db.Model):
    __tablename__ = 'sponsor'
    sponsor_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('sponsor_profile', uselist=False))
    company_name = db.Column(db.String(255))
    industry = db.Column(db.String(255))
    status = db.Column(db.String(255))
    budget = db.Column(db.Float)
    user = db.relationship('User', backref=db.backref('sponsor_profile', uselist=False))
    campaigns = db.relationship('Campaign', backref='sponsor', lazy='dynamic')
    ads = db.relationship('Ad', backref='sponsor', lazy='dynamic')

    @property
    def sponsor_name(self):
        return self.user.username

    @property
    def sponsor_email(self):
        return self.user.email


    def serialize(self):
        return {
            'sponsor_id': self.sponsor_id,
            'sponsor_name': self.sponsor_name,
            'sponsor_email': self.sponsor_email,
            'company_name': self.company_name,
            'industry': self.industry,
            'status':self.status,
            'budget': self.budget,
            'user': self.user.serialize() if self.user else None,
            'campaigns': [campaign.serialize() for campaign in self.campaigns],
            'ads': [ad.serialize() for ad in self.ads]
        }

    
    def get_all_sponsors():
        sponsors = User.query.all()
        return sponsors

class Influencer(db.Model):
    __tablename__ = 'influencer'
    influencer_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('influencer_profile', uselist=False))
    category = db.Column(db.String(255))
    niche = db.Column(db.String(255))
    reach = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('influencer_profile', uselist=False))
    ad_requests = db.relationship('AdRequest', backref='influencer', lazy='dynamic')

    @property
    def influencer_name(self):
        return self.user.username

    @property
    def influencer_email(self):
        return self.user.email

    def serialize(self):
        return {
            'influencer_id': self.influencer_id,
            'influencer_name': self.influencer_name,
            'influencer_email': self.influencer_email,
            'category': self.category,
            'niche': self.niche,
            'reach': self.reach,
            'user': self.user.serialize() if self.user else None,
            'ad_requests': [ad_request.serialize() for ad_request in self.ad_requests]
        }
    
    def get_all_influencers():
        influencers = User.query.all()
        return influencers


class Campaign(db.Model):
    __tablename__ = 'campaign'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    sponsor_id = db.Column(db.Integer, db.ForeignKey('sponsor.sponsor_id'))
    description = db.Column(db.Text)
    status = db.Column(db.String(255))
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    campaign_img = db.Column(db.String(255))
    budget = db.Column(db.Float)
    visibility = db.Column(db.String(255))
    goals = db.Column(db.String(255))
    delete = db.Column(db.Boolean, default=False)
    ads = db.relationship('Ad', backref='campaign', lazy='dynamic')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'sponsor_id': self.sponsor_id,
            'description': self.description,
            'status': self.status,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'updated_at': self.updated_at,
            'campaign_img': self.campaign_img,
            'budget': self.budget,
            'visibility': self.visibility,
            'goals': self.goals,
            'delete': self.delete,
            'ads': [ad.serialize() for ad in self.ads]
        }
    
    # def get_all(self):

    def admin_delete(id):
        Campaign = Campaign.query.filter_by(id=id).first()
        if not Campaign:
            return "No Campaign found by that id", False
        # delete category row with sql
        db.session.delete(Campaign)
        db.session.commit()
        return "Campaign deleted successfully", True
    
class Ad(db.Model):
    __tablename__ = 'ad'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    content = db.Column(db.Text)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'))
    sponsor_id = db.Column(db.Integer, db.ForeignKey('sponsor.sponsor_id'))
    start_date = db.Column(db.DateTime)
    requirements = db.Column(db.Text)
    budget = db.Column(db.Float)
    img = db.Column(db.String(255))
    status = db.Column(db.Boolean)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    target_audience = db.Column(db.String(255))
    delete = db.Column(db.Boolean, default=False)
    ad_requests = db.relationship('AdRequest', backref='ad', lazy='dynamic')

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'content': self.content,
            'campaign_id': self.campaign_id,
            'sponsor_id': self.sponsor_id,
            'start_date': self.start_date,
            'requirements': self.requirements,
            'budget': self.budget,
            'img': self.img,
            'status': self.status,
            'updated_at': self.updated_at,
            'target_audience': self.target_audience,
            'delete': self.delete,
            
        }
    
    def admin_delete(id):
        ad = Ad.query.filter_by(id=id).first()
        if not ad:
            return "No Advertisement found by that id", False
        # delete product row with sql
        db.session.delete(ad)
        db.session.commit()
        return "Advertisement deleted successfully", True


class AdRequest(db.Model):
    __tablename__ = 'ad_request'
    id = db.Column(db.Integer, primary_key=True)
    ad_id = db.Column(db.Integer, db.ForeignKey('ad.id'))
    sponsor_id = db.Column(db.Integer, db.ForeignKey('sponsor.sponsor_id'))
    influencer_id = db.Column(db.Integer, db.ForeignKey('influencer.influencer_id'))
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'))
    message = db.Column(db.Text)
    status = db.Column(db.String(255))
    request_date = db.Column(db.DateTime, default=datetime.utcnow)
    requirements = db.Column(db.Text)
    payment = db.Column(db.Float)

    def serialize(self):
        return {
            'id': self.id,
            'ad_id': self.ad_id,
            'sponsor_id': self.sponsor_id,
            'influencer_id': self.influencer_id,
            'campaign_id': self.campaign_id,
            'message': self.message,
            'status': self.status,
            'request_date': self.request_date,
            'requirements': self.requirements,
            'payment': self.payment
        }
    def ad_delete(id):
        adreq = AdRequest.query.filter_by(id=id).first()
        if not adreq:
            return "No Ad Request found by that id", False
        # delete product row with sql
        db.session.delete(adreq)
        db.session.commit()
        return "Ad Request deleted successfully", True



class DailyVisit(db.Model):
    __tablename__ = 'daily_visits'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    role= db.Column(db.String(20))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column(db.Date)
    user = db.relationship('User', backref='visits')

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
