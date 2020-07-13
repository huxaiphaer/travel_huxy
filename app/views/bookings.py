from flask import jsonify, make_response
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_restful import Resource

from app.extensions import db
from app.model.tour_packages_model import TourPackages, User, BookTour


class Bookings(Resource):

    def book_tour(self, tour_id):
        tours = TourPackages.query.filter_by(id=tour_id).first()
        user = User.query.filter_by(email=get_jwt_identity()).first()

        user_exists = BookTour.query.filter_by(user=user.id).first()

        if user_exists:
            return jsonify({
                'message': 'Sorry please, you can\'t book more that once.'
            })

        if tours is None:
            return jsonify({
                'message': 'Tour package is not found.'
            })

        capacity = int(tours.capacity)
        if capacity is 0:
            return make_response(jsonify({
                'message': 'Sorry unfortunately,the capacity for this tour is done. :('
            }), 404)

        tours.capacity = capacity - 1
        bookings = BookTour(tour=tours.id, user=user.id)
        db.session.add(bookings)
        db.session.commit()

        return make_response(jsonify({
            'message': 'booking made successfully'
        }), 201)

    def delete_booking(self, tour_id):

        booking = BookTour.query.filter_by(tour=tour_id).first()
        if booking is None:
            message = {
                'message': 'The booking is not found'
            }

            return make_response(jsonify(message), 200)
        tours = TourPackages.query.filter_by(id=tour_id).first()

        if tours is None:
            return jsonify({
                'message': 'Tour package is not found.'
            })

        capacity = int(tours.capacity)
        tours.capacity = capacity + 1
        BookTour.query.filter_by(tour=tour_id).delete()
        db.session.commit()

        message = {
            'message': 'The booking has been cancelled'
        }

        return make_response(jsonify(message), 204)

    @jwt_required
    def post(self, tour_id):
        return self.book_tour(tour_id)

    def delete(self, tour_id):
        return self.delete_booking(tour_id)
