from datetime import datetime

from flask import jsonify, make_response
from flask_restful import Resource, reqparse

from app.extensions import db
from app.model.marshallow_models import TourPackagesSchema
from app.model.tour_packages_model import TourPackages, Destinations, AvailableDates
from app.utils.json_utils import filter_args_and_json_custom_creator
from flask_jwt_extended import JWTManager, jwt_required


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

    @jwt_required
    def get_all_tours(self):

        tours = TourPackages.query.all()
        tour_schema = TourPackagesSchema(many=True)
        dump_data = tour_schema.dump(tours)

        output = jsonify({'data': dump_data})
        return output

    @jwt_required
    def post(self):
        return self.insert_tour_packages()

    @jwt_required
    def get(self):
        return self.get_all_tours()


class SingleTour(Resource):

    def update_tour(self, tour_id):

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

        format_dest = filter_args_and_json_custom_creator(destinations)
        format_dates = filter_args_and_json_custom_creator(available_dates)

        tours = TourPackages.query.filter_by(id=tour_id).first()
        tours.name = name
        tours.description = description
        tours.price = price
        tours.capacity = capacity

        dest = Destinations.query.filter_by(tour_Packages=tour_id).all()
        avail = AvailableDates.query.filter_by(tour_date=tour_id).all()

        for d in range(0, len(dest)):
            i = int(d)
            dest[i].location = format_dest[i]['location']
            dest[i].tour_type = format_dest[i]['tour_type']
            dest[i].danger_type = format_dest[i]['danger_type']

        for a in range(0, len(avail)):
            i = int(a)
            avail[i].date_available = format_dates[i]['date_available']

        db.session.commit()
        message = {
            'success': 'tour package updated created'
        }
        return make_response(jsonify(message), 200)

    def delete_tour(self, tour_id):
        TourPackages.query.filter_by(id=tour_id).delete()
        Destinations.query.filter_by(tour_Packages=tour_id).delete()
        AvailableDates.query.filter_by(tour_date=tour_id).delete()

        db.session.commit()

        message = {
            'success': 'tour package with id {id} deleted'.format(id=tour_id)
        }

        return make_response(jsonify(message), 204)

    def get_tour_by_id(self, tour_id):
        tours = TourPackages.query.filter_by(id=tour_id).first()

        if tours is None:
            return make_response(jsonify(message="tour package is not available"), 200)
        tour_schema = TourPackagesSchema()
        dump_data = tour_schema.dump(tours)
        output = jsonify({'data': dump_data})
        return output

    @jwt_required
    def put(self, tour_id):
        return self.update_tour(tour_id)

    @jwt_required
    def delete(self, tour_id):
        return self.delete_tour(tour_id)

    @jwt_required
    def get(self, tour_id):
        return self.get_tour_by_id(tour_id)


class BookTour(Resource):

    def book_tour(self):
        pass

    def book_tour(self):
        pass