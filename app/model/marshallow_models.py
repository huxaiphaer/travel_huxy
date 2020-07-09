from app.extensions import ma
from app.model.tour_packages_model import TourPackages, Destinations, AvailableDates


class DestinationSchema(ma.Schema):
    class Meta:
        model = Destinations
        fields = ('id', 'location', 'danger_type')


class AvailableDatesSchema(ma.Schema):
    class Meta:
        model = AvailableDates
        fields = ('id', 'date_')


class TourPackagesSchema(ma.Schema):
    class Meta:
        model = TourPackages
        fields = ('id', 'name', 'description', 'price', 'capacity')
