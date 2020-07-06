from datetime import datetime

from app.extensions import db


class TourPackages(db.Model):
    __tablename__ = 'tourpackage'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.TEXT)
    price = db.Column(db.Float)
    destination_id = db.relationship('Destinations', backref='destination_id')
    capacity = db.Column(db.Integer)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'capacity': self.capacity
        }


class Destinations(db.Model):
    __tablename__ = 'destinations'

    id = db.Column(db.Integer, primary_key=True)
    tour_Packages = db.Column(db.Integer, db.ForeignKey('tourpackage.id'))
    location = db.Column(db.String(50))
    danger_type = db.Column(db.String(50))
