from flask import Flask, Blueprint
from .api.v1 import version_1 as v1
#local imports
from instance.config import app_config



def create_app(config_name='development'):
    app = Flask(__name__, instance_relative_config = True)
    app.url_map.strict_slashes = False
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')



    app.register_blueprint(v1)
    return app






















# from flask_api import FlaskAPI
# from .api.v1 import version_1 as v1
# from instance.config import app_config

# def create_app(config_name):
#     app=FlaskAPI(__name__,instance_relative_config=True)
    
#     app.config.from_pyfile('config.py')
#     app.register_blueprint(v1)
#     return app







# from flask import Flask
# from flask_restful import Api,Resource
# #local imports


# # from  .api.v1.views.redflag_views import Redflags,RedflagsSpecific

# def create_app():
#     app=Flask(__name__)
#     api = Api(app)
#     api.add_resource(Redflags,'/redflags')
#     api.add_resource(RedflagsSpecific,'/redflags/<int:item_id>')
#     return app