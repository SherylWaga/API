from flask import Flask
from flask_restful import Api,Resource
#local imports


from  .api.v1.views.redflag_views import Redflags,RedflagsSpecific

def create_app():
    app=Flask(__name__)
    api = Api(app)
    api.add_resource(Redflags,'/redflags')
    api.add_resource(RedflagsSpecific,'/redflags/<int:item_id>')
    return app