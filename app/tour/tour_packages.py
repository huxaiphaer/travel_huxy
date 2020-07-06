from flask_restful import Resource, reqparse
from flask import jsonify
from app.extensions import db

from app.model.tour_packages import TourPackages, Destinations


class GetTourPackages(Resource):

    def insert_tour_packages(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('description', type=str, required=True)
        parser.add_argument('price', type=float, required=True)
        parser.add_argument('destination_location', type=str)
        parser.add_argument('destination_danger_type', type=str)
        parser.add_argument('capacity', type=int, required=True)
        args = parser.parse_args()

        name = args['name']
        description = args['description']
        price = args['price']
        capacity = args['capacity']
        destination_location = args['destination_location']
        destination_danger_type = args['destination_danger_type']

        add_tour = TourPackages(name=name, description=description, price=price,
                                capacity=capacity)

        add_destination = Destinations(
            location=destination_location,
            danger_type=destination_danger_type
        )

        add_tour.destination_id.append(add_destination)

        db.session.add(add_tour)
        db.session.commit()

        return jsonify(add_tour.serialize)

    def post(self):
        return self.insert_tour_packages()
