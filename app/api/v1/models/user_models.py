
from flask import request,jsonify
from flask_restful import Resource
#local import
from app.api.v1.views.user_views import user
class save_user(Resource):
     def get(self): 
        users = user().view_users()
        return users
     def post(self):   
        new_user= user().register_user()
        return new_user






















