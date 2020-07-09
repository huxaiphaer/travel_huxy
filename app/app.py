from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_restful import Api
from app.extensions import db

from app.views.tour_packages import GetTourPackages


def register_extensions(app):
    """Register Flask Extensions"""
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    app.secret_key = "huxy"
    db.init_app(app)
    Migrate(app, db)

    return None


def create_app():
    app = Flask(__name__)
    register_extensions(app)
    return app


application = create_app()

api = Api(application)
api.add_resource(GetTourPackages, '/api/v1/tourpackages')
