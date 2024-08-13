from flask import current_app as app
from flask import current_app as app, jsonify, request, render_template, send_file
from flask.json import dump
from flask_security import auth_required, roles_required
from sqlalchemy import or_
from werkzeug.security import check_password_hash, generate_password_hash
from flask_restful import marshal, fields
from database.models import User, db,user_datastore

@app.get('/')
def index():
    return render_template('index.html')


@app.post('/sponsor-login')
def sponsor_login():
    data = request.get_json()
    email = data.get('email')
    if not email:
        return jsonify({"message": "Email not provided"}), 400

    user = user_datastore.find_user(email=email)

    if "sponsor" not in user.roles:
        return jsonify({"message": "User Not a Sponsor"}), 404

    if not user:
        return jsonify({"message": "User Not Found"}), 404

    if check_password_hash(user.password, data.get("password")):
        return jsonify({"token": user.get_auth_token(), "email": user.email, "role": user.roles[0].name})
    else:
        return jsonify({"message": "Wrong Password"}), 400
    
@app.post('/admin-login')
def admin_login():
    data = request.get_json()
    email = data.get('email')
    if not email:
        return jsonify({"message": "Email not provided"}), 400

    user = user_datastore.find_user(email=email)

    if "admin" not in user.roles:
        return jsonify({"message": "User Not a Sponsor"}), 404

    if not user:
        return jsonify({"message": "User Not Found"}), 404

    if check_password_hash(user.password, data.get("password")):
        return jsonify({"token": user.get_auth_token(), "email": user.email, "role": user.roles[0].name})
    else:
        return jsonify({"message": "Wrong Password"}), 400

@app.post('/influencer-login')
def influencer_login():
    data = request.get_json()
    email = data.get('email')
    if not email:
        return jsonify({"message": "Email not provided"}), 400

    user = user_datastore.find_user(email=email)
    if "influencer" not in user.roles:
        return jsonify({"message": "User Not a influencer"}), 404

    if not user:
        return jsonify({"message": "User Not Found"}), 404

    if check_password_hash(user.password, data.get("password")):
        return jsonify({"token": user.get_auth_token(), "email": user.email, "role": user.roles[0].name})
    else:
        return jsonify({"message": "Wrong Password"}), 400


@app.post('/user-register')
def user_register():
    data = request.get_json()
    email = data.get('email')
    name = data.get('name')
    password = data.get('password')
    if not email:
        return jsonify({"message": "email not provided"}), 400

    if not name:
        return jsonify({"message": "name not provided"}), 400

    if not password:
        return jsonify({"message": "password not provided"}), 400

    user_exists = User.query.filter_by(email=email).count()
    if(user_exists):
        return {"message":"Email already taken, use another email"},401
    user = user_datastore.create_user(email=email, name=name, password=generate_password_hash(password), active=True,
                                 roles=["member"])

    db.session.add(user)

    db.session.commit()
    return jsonify({"token": user.get_auth_token(), "email": user.email, "role": user.roles[0].name}),201
