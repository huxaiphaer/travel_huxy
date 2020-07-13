import os
import sys
from datetime import datetime

from app.extensions import db
from app.model.weather_model import WeatherForecast

sys.path.append(os.getcwd())
from flask_testing import TestCase
import json
from app.app import application
from app.config.config import app_config


class BaseTestCase(TestCase):

    def create_app(self):
        """
        Create an instance of the app with the testing configuration
        """
        application.config.from_object(app_config["testing"])
        return application

    def setUp(self):
        db.create_all()
        weather = WeatherForecast(weather_type="Sunny",
                                  date_time=datetime(2012, 3, 3, 10, 10, 10),
                                  description="Its sunny",
                                  name="Sunny ",
                                  latitude="34.790878",
                                  longitude="48.570728"
                                  )
        db.session.add(weather)
        db.session.commit()
        self.client = application.test_client(self)

    def tearDown(self):
        """
        Drop the database
        """

    def register_user(self, email, first_name, last_name, password):
        """
        Method for registering a user with dummy data
        """
        return self.client.post(
            'api/v1/register',
            data=json.dumps(dict(
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=password
            )
            ),
            content_type='application/json'
        )

    def login_user(self, email, password):
        """
        Method for logging a user with dummy data
        """
        return self.client.post(
            'api/v1/login',
            data=json.dumps(
                dict(
                    email=email,
                    password=password
                )
            ),
            content_type='application/json'
        )

    def get_token(self):
        """
        Returns a user token
        """
        self.register_user("jau20@gmail.com", "buki", "jau", "123456789")
        response = self.login_user("jau20@gmail.com", "123456789")
        data = json.loads(response.data.decode())
        return data['access_token']

    def add_tour(self, name, description, price, available_dates, destinations, capacity, token):
        """
         Create tour packages
        """
        return self.client.post(
            '/api/v1/tourpackages',
            data=json.dumps(
                dict(
                    name=name,
                    description=description,
                    price=price,
                    available_dates=available_dates,
                    destinations=destinations,
                    capacity=capacity
                )
            ),
            content_type='application/json',
            headers=({"Authorization": "Bearer {token}".format(token=token)})
        )

    def get_tour_packages(self, token):
        """
        function to return get
        """
        return self.client.get('/api/v1/tourpackages',
                               headers=({"Authorization": "Bearer {token}".format(token=token)}))

    def get_single_tour_package(self, id, token):
        """
        get
        :return:
        """

        return self.client.get('/api/v1/tourpackages/{}'.format(id),
                               headers=({"Authorization": "Bearer {token}".format(token=token)}))

    def update_tour_package(self, id, name, description, price, available_dates, destinations, capacity, token):
        """
        update tour package
        :return:
        """
        return self.client.get('/api/v1/tourpackages/{}'.format(id),
                               data=json.dumps(
                                   dict(
                                       name=name,
                                       description=description,
                                       price=price,
                                       available_dates=available_dates,
                                       destinations=destinations,
                                       capacity=capacity
                                   )
                               ),
                               headers=({"Authorization": "Bearer {token}".format(token=token)}))

    def get_tours_by_date(self, first_date, last_date, token):
        """
        Get tours by Date
        :return:
        """

        return self.client.get('/api/v1/tourpackages/{}/{}'.format(first_date, last_date),
                               headers=({"Authorization": "Bearer {token}".format(token=token)}))

    def add_booking(self, id, token):
        """
        Book for an existing tour package
        :return:
        """

        return self.client.post('/api/v1/booking/{}'.format(id),
                                headers=({"Authorization": "Bearer {token}".format(token=token)}))

    def get_weather_data(self, lat, lon, token):
        """
        Get weather data
        :return:
        """

        return self.client.get(
            '/api/v1/weather/{}/{}'.format(lat, lon),
            headers=({"Authorization": "Bearer {token}".format(token=token)})
        )
