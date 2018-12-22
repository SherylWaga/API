from flask import request,jsonify,make_response
from flask_restful import Resource
#local import
from app.api.v1.views.redflag_views import Instance
class Redflags(Resource):
    def get(self):
        redflags = Instance().view_redflags()
        return redflags
    def post(self):
        new_post= Instance().create_redflag()
        return new_post
class RedflagsSpecific(Resource):
    def get(self, item_id):
        specific_data = Instance().specific(item_id)
        return specific_data
    def delete(self,item_id):
        return Instance().delete_redflag(item_id)
    def put(self,item_id):
        return Instance().edit_redflag(item_id)
    
