from datetime import datetime

from app.extensions import db


class TourPackages(db.Model):
    __tablename__ = 'tourpackage'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.TEXT)
    price = db.Column(db.Float)
    destinations = db.relationship('Destinations', backref='destination_id', lazy='dynamic')
    available_dates = db.relationship('AvailableDates', backref='available_date_id', lazy='dynamic')
    capacity = db.Column(db.Integer)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)


class Destinations(db.Model):
    __tablename__ = 'destinations'

    id = db.Column(db.Integer, primary_key=True)
    tour_Packages = db.Column(db.Integer, db.ForeignKey('tourpackage.id'))
    location = db.Column(db.String(50))
    tour_type = db.Column(db.String(50))
    danger_type = db.Column(db.String(50))


class AvailableDates(db.Model):
    __tablename__ = 'availabledates'

    id = db.Column(db.Integer, primary_key=True)
    date_available = db.Column(db.String(50))
    tour_date = db.Column(db.Integer, db.ForeignKey('tourpackage.id'))
