from flask import jsonify, make_response
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
from flask_restful_swagger_3 import swagger

from app.extensions import db
from app.model.tour_packages_model import User


class UserRegistration(Resource):

    @swagger.doc({
        'tags': ['user'],
        'description': 'Registers a user',
        'parameters': [
            {
                'name': 'user_id',
                'description': 'User identifier',
                'in': 'path',
                'schema': {
                    'type': 'integer'
                }
            }
        ],
        'responses': {
            '200': {
                'description': 'User',
                'content': {
                    'application/json': {
                        'schema': User,
                        'examples': {
                            'application/json': {
                                'id': 1,
                                'message': 'User created successfully'
                            }
                        }
                    }
                }
            }
        }
    })
    def register_user(self):

        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('first_name', type=str, required=True)
        parser.add_argument('last_name', type=str, required=True)
        parser.add_argument('password', type=str, required=True)
        args = parser.parse_args()

        email = args['email']
        test = User.query.filter_by(email=email).first()
        if test:
            message = {
                'message': 'That email already exist'
            }
            return make_response(jsonify(message), 409)
        else:
            first_name = args['first_name']
            last_name = args['last_name']
            password = args['password']
            user = User(first_name=first_name, last_name=last_name, password=password, email=email)
            db.session.add(user)
            db.session.commit()

            message = {
                'message': 'User created successfully'
            }
            return make_response(jsonify(message), 201)

    def post(self):
        return self.register_user()


class UserLogin(Resource):

    def login_user(self):

        parser = reqparse.RequestParser()
        parser.add_argument('email', type=str, required=True)
        parser.add_argument('password', type=str)
        args = parser.parse_args()

        email = args['email']
        password = args['password']

        test = User.query.filter_by(email=email, password=password).first()

        if test:
            access_token = create_access_token(identity=email)
            return jsonify(message="Login succeeded", access_token=access_token)
        else:
            return jsonify(message="Email or password is wrong")

    def post(self):

        return self.login_user()
