from flask import request,jsonify
from flask_restful import Resource
#local import
from app.api.v1.models.redflag_models import Locate
class Redflags(Resource):
    def post(self):
        new_post= Locate().new()
        return new_post

    


















