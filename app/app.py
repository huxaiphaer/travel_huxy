from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_restful import Api

from app.extensions import db
from app.views.tour_packages import GetTourPackages, SingleTour
from app.views.user import UserRegistration, UserLogin


def register_extensions(app):
    """Register Flask Extensions"""
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.secret_key = "huxy"
    db.init_app(app)
    Migrate(app, db)
    JWTManager(app)
    return None


def create_app():
    app = Flask(__name__)
    register_extensions(app)
    return app


application = create_app()

api = Api(application)
api.add_resource(GetTourPackages, '/api/v1/tourpackages')
api.add_resource(SingleTour, '/api/v1/tourpackages/<tour_id>')
api.add_resource(UserRegistration, '/api/v1/register')
api.add_resource(UserLogin, '/api/v1/login')
