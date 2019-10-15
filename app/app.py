from flask import Flask, Blueprint, request
from instance.config import app_config
from app.user.user import user

def create_app(config_name):
    app = Flask("Flights", instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    print(app_config[config_name])
    #app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.register_blueprint(user)
    #db.init_app(app)
    return app
