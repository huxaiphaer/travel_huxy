from datetime import datetime

from flask import jsonify
from flask_restful import Resource, reqparse

from app.extensions import db
from app.model.marshallow_models import TourPackagesSchema
from app.model.tour_packages_model import TourPackages, Destinations, AvailableDates


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
        parser.add_argument('destination_location', type=str)
        parser.add_argument('destination_danger_type', type=str)
        parser.add_argument('capacity', type=int, required=True)
        parser.add_argument('available_dates', type=str, action='append', required=True)
        args = parser.parse_args()
        name = args['name']
        description = args['description']
        price = args['price']
        capacity = args['capacity']
        destination_location = args['destination_location']
        destination_danger_type = args['destination_danger_type']
        available_dates = args['available_dates']
        formatted_list_of_dates = str(available_dates)

        for i in available_dates:
            if not self.validate_date(i):
                return jsonify({"error": "Please enter the correct date format YYYY-MM-DD"})

        add_tour = TourPackages(name=name, description=description, price=price,
                                capacity=capacity)

        add_destination = Destinations(
            location=destination_location,
            danger_type=destination_danger_type
        )

        add_available_dates = AvailableDates(
            date_=formatted_list_of_dates
        )

        add_tour.destination_id.append(add_destination)
        add_tour.available_date_id.append(add_available_dates)

        db.session.add(add_tour)
        db.session.commit()

        return jsonify({
            'success': 'tour package successfully created'
        })

    def get_all_tours(self):
        # tours = db.session.query(TourPackages).all()
        tours = db.session.query(TourPackages.name, TourPackages.description, TourPackages.price,
                                 TourPackages.capacity,
                                 Destinations.location,
                                 Destinations.danger_type, AvailableDates.date_).join(
            Destinations).join(AvailableDates).all()

        tour_schema = TourPackagesSchema()

        dump_data = tour_schema.dump(tours)
        print("dump data ", dump_data)
        print("query --", tours)

        output = jsonify(dump_data)

        return output

    def post(self):
        return self.insert_tour_packages()

    def get(self):
        return self.get_all_tours()
