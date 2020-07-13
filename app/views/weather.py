from flask import jsonify
from flask_jwt_extended import jwt_required
from flask_restful import Resource
from sqlalchemy import desc

from app.model.marshallow_models import WeatherSchema
from app.model.weather_model import WeatherForecast


class Weather(Resource):

    @jwt_required
    def get_weather_data(self, latitude, longitude):
        """
        :param self:
        :param latitude:
        :param longitude:
        :return json
        """
        query = WeatherForecast.query.filter_by(latitude=latitude, longitude=longitude).order_by(
            desc(WeatherForecast.date_time)).limit(5).all()
        weather_schema = WeatherSchema(many=True)
        dump_data = weather_schema.dump(query)
        output = jsonify({'data': dump_data})
        return output

    def get(self, latitude, longitude):
        return self.get_weather_data(latitude=latitude, longitude=longitude)
