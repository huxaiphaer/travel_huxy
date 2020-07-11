from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from celery import Celery

db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()
celery = Celery()
