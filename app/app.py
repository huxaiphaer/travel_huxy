from celery import Celery
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from flask_restful import Api
import os
from app.extensions import db
from app.views.bookings import Bookings
from app.views.tour_packages import GetTourPackages, SingleTour, GetTourPackagesByDate
from app.views.user import UserRegistration, UserLogin
from app.views.weather import Weather


def register_extensions(app):
    """Register Flask Extensions"""
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = os.environ['SECRET_KEY']
    db.init_app(app)
    Migrate(app, db)
    JWTManager(app)
    Celery(app)
    return None


def create_app():
    app = Flask(__name__)
    register_extensions(app)
    return app


application = create_app()

api = Api(application)
api.add_resource(GetTourPackages, '/api/v1/tourpackages')
api.add_resource(GetTourPackagesByDate, '/api/v1/tourpackages/<first_date>/<end_date>')
api.add_resource(SingleTour, '/api/v1/tourpackages/<tour_id>')
api.add_resource(UserRegistration, '/api/v1/register')
api.add_resource(UserLogin, '/api/v1/login')
api.add_resource(Bookings, '/api/v1/booking/<tour_id>')
api.add_resource(Weather, '/api/v1/weather/<latitude>/<longitude>')
