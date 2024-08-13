import base64
import random
from datetime import datetime
from io import BytesIO
import matplotlib
from flask_security import verify_password, login_user, roles_accepted, current_user, logout_user
import matplotlib.pyplot as plt
from flask import request, jsonify
from flask_restful import Resource, Api, reqparse, fields, marshal
from flask_security import current_user, auth_required, roles_required,verify_password,login_user,roles_accepted , hash_password
from sqlalchemy import text
from werkzeug.utils import secure_filename
from flask import jsonify, request, make_response

from database.models import *

class login(Resource):
    def post(self):
        data = request.get_json()
        email = data['email']
        password = data['password']
        user = user_datastore.find_user(email=email)
        
        if user:
            if verify_password(password, user.password):
                login_user(user)
                db.session.commit()
                token = user.get_auth_token()
                role = 'admin' if current_user.has_role('admin') else 'sponsor' if current_user.has_role('sponsor') else 'influencer'
                
                response_data = {
                    'token': token,
                    'email': user.email,
                    'username':user.username,
                    'user_id': user.id,
                    'role': role,
                    'message': 'login successful'
                }
                
                if role == 'influencer':
                    influencer = Influencer.query.filter_by(user_id=user.id).first()
                    response_data.update({
                        'influencer_id': influencer.influencer_id,
                        'username': user.username,
                        'category': influencer.category,
                        'niche': influencer.niche,
                        'reach': influencer.reach
                    })
                
                elif role == 'sponsor':
                    sponsor = Sponsor.query.filter_by(user_id=user.id).first()
                    response_data.update({
                        'sponsor_id': sponsor.sponsor_id,
                        'username': user.username,
                        'Company_name': sponsor.company_name,
                        'Industry': sponsor.industry,
                        'budget': sponsor.budget,
                        'status':sponsor.status,
                    })

                return make_response(jsonify(response_data), 200)
            return make_response(jsonify({'message': 'password doesnt match'}), 401)
        return make_response(jsonify({'message': 'user not present', 'email': email}), 404)
    
class register(Resource):
    def post(self):
        data = request.get_json()
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')
        role = data.get('role')
        sponsor_details = data.get('sponsor_details', {})
        influencer_details = data.get('influencer_details', {})

        if not email:
            return make_response(jsonify({"message": "Email is required"}), 400)
        if not password:
            return make_response(jsonify({"message": "Password is required"}), 400)
        if not role:
            return make_response(jsonify({"message": "Role is required"}), 400)
        if not username:
            return make_response(jsonify({"message": "Username is required"}), 400)

        user = user_datastore.find_user(email=email)
        if user:
            return make_response(jsonify({"message": "User already present", "email": user.email}), 400)

        user = user_datastore.create_user(email=email, username=username, password=hash_password(password))
        db.session.flush()  # Ensure the user ID is generated
        token = user.get_auth_token()

        if role == 'sponsor':
            sponsor = Sponsor(
                user_id=user.id,
                company_name=sponsor_details.get('company_name', ''),
                industry=sponsor_details.get('industry', ''),
                budget=sponsor_details.get('budget', 0),
                status=sponsor_details.get('status', ''),
            )
            db.session.add(sponsor)
            user_datastore.add_role_to_user(user, 'sponsor')
            db.session.commit()
            return make_response(jsonify({"message": "Sponsor created successfully","user_id":user.id,"sponsor_id":sponsor.sponsor_id, "email": user.email,"status": sponsor.status,"username":user.username,"company_name": sponsor.company_name,"industry":sponsor.industry,"budget":sponsor.budget, "token": token, "role": role}), 201)
        elif role == 'influencer':
            influencer = Influencer(
                user_id=user.id,
                category=influencer_details.get('category', ''),
                niche=influencer_details.get('niche', ''),
                reach=influencer_details.get('reach', 0)
            )
            db.session.add(influencer)
            user_datastore.add_role_to_user(user, 'influencer')
            db.session.commit()
            return make_response(jsonify({"message": "Influencer created successfully","user_id":user.id,"influencer_id":influencer.influencer_id, "email": user.email,"username":user.username,"category": influencer.category,"niche":influencer.niche,"reach":influencer.reach, "token": token, "role": role}), 201)
        else:
            return make_response(jsonify({"message": "Invalid role"}), 400)

       
    
class logout(Resource):
    @roles_accepted('admin', 'sponsor', 'influencer')
    def post(self):
        user = user_datastore.find_user(id=current_user.id)
        if not user:
            return make_response(jsonify({"message": "No user found by that id"}), 404)
        logout_user(user)
        db.session.commit()
        return make_response(jsonify({"message": "user logged out successfully", "email": user.email}), 200)
