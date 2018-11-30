from flask import Blueprint
from flask_restful import Api

from .views.redflag_views import Redflags,RedflagsSpecific

version_1=Blueprint('api_v1',__name__,url_prefix='/api/v1')
api=Api(version_1)
api.add_resource(Redflags,'/redflags')
api.add_resource(RedflagsSpecific,'/redflags/<int:item_id>')