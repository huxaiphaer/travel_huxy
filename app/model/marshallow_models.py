from marshmallow import fields

from app.extensions import ma, db
from app.model.tour_packages_model import TourPackages, Destinations, AvailableDates
from app.model.weather_model import WeatherForecast


class DestinationSchema(ma.Schema):
    class Meta:
        model = Destinations
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    location = fields.String(required=True)
    danger_type = fields.String(required=True)


class AvailableDatesSchema(ma.Schema):
    class Meta:
        model = AvailableDates
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    date_available = fields.String(required=True)


class TourPackagesSchema(ma.Schema):
    class Meta:
        model = TourPackages
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    name = fields.String(required=True)
    description = fields.String(required=True)
    price = fields.Float(required=True)
    capacity = fields.Number(required=True)
    destinations = fields.Nested(DestinationSchema, many=True)
    available_dates = fields.Nested(AvailableDatesSchema, many=True)


class WeatherSchema(ma.Schema):
    class Meta:
        model = WeatherForecast
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    weather_type = fields.String(required=True)
    date_time = fields.String(required=True)
    description = fields.String(required=True)
    latitude = fields.String(required=True)
    longitude = fields.String(required=True)
    name = fields.String(required=True)
