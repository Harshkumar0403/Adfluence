from app import create_app
from database.models import user_datastore

from app import app

def generate_sample_token():
    tokens = {"Admin": "", "Sponsor": "", "Influencer": ""}
    admin_user = user_datastore.find_user(email='admin@example.com')
    sponsor_user = user_datastore.find_user(email='sponsor@example.com')
    influencer_user = user_datastore.find_user(email='influencer@example.com')

    if admin_user:
        tokens["Admin"] = admin_user.get_auth_token()

    if sponsor_user:
        tokens["Sponsor"] = sponsor_user.get_auth_token()
    
    if influencer_user:
        tokens["Influencer"] = influencer_user.get_auth_token()
    
    return tokens

with app.app_context():
    tokens = generate_sample_token()
    with open('tokens.txt', 'w') as file:
        for role, token in tokens.items():
            file.write(f"{role} token: {token}\n")