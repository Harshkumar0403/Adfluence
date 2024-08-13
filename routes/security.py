from flask_security import SQLAlchemyUserDatastore
from database.models import db, User, Role
from flask_security import Security, login_user, verify_password
from database.models import user_datastore

security = Security()

def login_fn(email, password):
    user = user_datastore.find_user(email=email)  
    if user:
        if verify_password(password, user.password):  
            login_user(user)
            db.session.commit()
            return user.get_auth_token()
        return 'Invalid password'
    return 'User not found'
