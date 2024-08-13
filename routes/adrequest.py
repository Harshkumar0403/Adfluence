from flask import request, jsonify, make_response
from flask_restful import Resource
from flask_security import roles_accepted,auth_required
from caching import cache
from datetime import datetime
from database.models import db, AdRequest, Ad, Campaign, Sponsor, Influencer

class AdRequestResource(Resource):

    @roles_accepted('admin', 'sponsor','influencer')
    def post(self):
        data = request.get_json()
        ad_id = data.get('ad_id')
        sponsor_id = data.get('sponsor_id')
        influencer_id = data.get('influencer_id')
        campaign_id = data.get('campaign_id')
        message = data.get('message')
        status = 'pending'
        requirements = data.get('requirements')
        payment = data.get('payment')

        ad_request = AdRequest(
            ad_id=ad_id,
            sponsor_id=sponsor_id,
            influencer_id=influencer_id,
            campaign_id=campaign_id,
            message=message,
            status=status,
            requirements=requirements,
            payment=payment,
            request_date=datetime.utcnow()
        )
        db.session.add(ad_request)
        db.session.commit()
        
        return make_response(jsonify({"message": "Ad request created successfully", "ad_request_id": ad_request.id}), 201)

    @roles_accepted('admin', 'sponsor', 'influencer')
    @cache.cached(timeout=20)
    @auth_required("token")
    def get(self):
        ad_requests = AdRequest.query.all()
        data = [ad_request.serialize() for ad_request in ad_requests]
        return make_response(jsonify({"data": data}), 200)
    

class AdRequestStatusResource(Resource):

    @roles_accepted('admin', 'sponsor', 'influencer')
    def put(self, id):
        ad_request = AdRequest.query.filter_by(id=id).first()
        if not ad_request:
            return make_response(jsonify({"message": "No ad request found by that id"}), 404)
        data = request.get_json()
        status = data.get('status')
        if status not in ['accepted', 'rejected','paid']:
            return make_response(jsonify({"message": "Invalid status"}), 400)
        ad_request.status = status
        db.session.commit()
        return make_response(jsonify({"message": f"Ad request {status} successfully", 'id': id}), 200)
    
    @roles_accepted('admin', 'sponsor','influencer')
    def delete(self, id):
        adreq = AdRequest.query.filter_by(id=id).first()
        if not adreq:
            return make_response(jsonify({"message": "No ad found by that id"}), 404)
  # Assuming there's a 'delete' attribute; might need adjustment
        db.session.delete(adreq)
        db.session.commit()
        return jsonify({"message": "delete specific adrequest", 'id': id})
    
    @cache.cached(timeout=20)
    @auth_required("token")
    def get(self, id):
        ad = AdRequest.query.filter_by(id=id).first()
        if not ad:
            return make_response(jsonify({"message": "No Ad Request found by that id"}), 404)
        ad = ad.serialize()
        return jsonify({"message": "get specific ad request", "data": ad})
