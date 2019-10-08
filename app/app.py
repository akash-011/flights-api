from flask import Flask
from flask_restplus import Api
from instance.config import app_config

api = Api(version='1.0', title='Flights API')

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #db.init_app(app)
    api.init_app(app)

    return app