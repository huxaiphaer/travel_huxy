from flask_marshmallow.sqla import SQLAlchemySchema, auto_field

from app.extensions import ma
from app.model.tour_packages_model import TourPackages, Destinations, AvailableDates


class TourPackagesSchema(ma.SQLAlchemySchema):
    class Meta:
        model = TourPackages
        load_instance = True

    id = auto_field()
    name = auto_field()
    description = auto_field()
    price = auto_field()
    capacity = auto_field()
    destination_id = auto_field()
    available_date_id = auto_field()


class DestinationSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Destinations
        load_instance = True

    id = auto_field()
    tour_Packages = auto_field()
    location = auto_field()
    danger_type = auto_field()


class AvailableDates(ma.SQLAlchemySchema):
    class Meta:
        model = AvailableDates
        load_instance = True

    id = auto_field()
    date_ = auto_field()
    tour_date = auto_field()
