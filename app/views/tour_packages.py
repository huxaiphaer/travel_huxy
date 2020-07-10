from datetime import datetime

from flask import jsonify
from flask_restful import Resource, reqparse

from app.extensions import db
from app.model.marshallow_models import TourPackagesSchema
from app.model.tour_packages_model import TourPackages, Destinations, AvailableDates
from app.utils.json_utils import filter_args_and_json_custom_creator


class GetTourPackages(Resource):

    def validate_date(self, date_text):
        try:
            if date_text != datetime.strptime(date_text, "%Y-%m-%d").strftime('%Y-%m-%d'):
                raise ValueError
            return True
        except ValueError:
            return False

    def insert_tour_packages(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('description', type=str, required=True)
        parser.add_argument('price', type=float, required=True)
        parser.add_argument('destinations', type=str, action='append')
        parser.add_argument('capacity', type=int, required=True)
        parser.add_argument('available_dates', type=str, action='append', required=True)
        args = parser.parse_args()

        name = args['name']
        description = args['description']
        price = args['price']
        destinations = args['destinations']
        available_dates = args['available_dates']
        capacity = args['capacity']

        dest_list = []
        available_dates_list = []

        format_dest = filter_args_and_json_custom_creator(destinations)
        format_dates = filter_args_and_json_custom_creator(available_dates)

        for d in format_dest:
            value = Destinations(location=d['location'], danger_type=d['danger_type'], tour_type=d['tour_type'])
            dest_list.append(value)

        for a in format_dates:
            value = AvailableDates(date_available=a['date'])
            available_dates_list.append(value)

        add_tour = TourPackages(name=name, description=description, price=price,
                                capacity=capacity, destinations=dest_list,
                                available_dates=available_dates_list)

        db.session.add(add_tour)
        db.session.commit()

        return jsonify({
            'success': 'tour package successfully created'
        })

    def get_all_tours(self):
        tours = db.session.query(TourPackages.name, TourPackages.description, TourPackages.price,
                                 TourPackages.capacity,
                                 Destinations.location,
                                 Destinations.danger_type, AvailableDates.date_).join(
            Destinations).join(AvailableDates).all()

        tour_schema = TourPackagesSchema(many=True)
        dump_data = tour_schema.dump(tours)
        output = jsonify(data=dump_data)
        return output

    def post(self):
        return self.insert_tour_packages()

    def get(self):
        return self.get_all_tours()
