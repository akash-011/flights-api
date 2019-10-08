from flask import Blueprint
from flask-restplus import Resource

users = Blueprint('users', __name__)

@users.route('/')
class Hello(Resource):

    def get(self):
        return {'hello', 'world'}
