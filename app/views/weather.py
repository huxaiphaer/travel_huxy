from flask_restful import Resource
import requests
from app.app import application
from app.config.redis_db import redis_db
from app.extensions import celery


class Weather(Resource):
    # Add periodic tasks
    celery_beat_schedule = {
        "time_scheduler": {
            "task": "run.paginate_requested_data",
            # Run every second
            "schedule": 300.0,
        }
    }
    # configure celery

    celery.conf.update(
        result_backend=application.config["CELERY_RESULT_BACKEND"],
        broker_url=application.config["CELERY_BROKER_URL"],
        timezone="UTC",
        task_serializer="json",
        accept_content=["json"],
        result_serializer="json",
        beat_schedule=celery_beat_schedule,
    )

    def insert_data(self, db, name, weather_data):
        """
        :param db:
        :param name:
        :param hyper_drive_rating:
        :return: None
        """

        db.hset('mydata', name, weather_data)

        return {"data": "data inserted successfully"}, 200

    def make_request(self, url_link, db):
        """
        Make request to the url and
        paginate
        @param url_link:
        @param db:
        @return: None
        """
        pagination = 1
        url = url_link
        params = {'page': pagination}
        r = requests.get(url, params=params)

        data = r.json()

        for i in data['results']:
            self.insert_data(db, str(i['name']), str(i['hyperdrive_rating']))

        while r.status_code == 200:
            try:
                pagination += 1
                params['page'] = pagination
                r = requests.get(url, params=params)
                data = r.json()
                for i in data['results']:
                    self.insert_data(db, str(i['name']), str(i['hyperdrive_rating']))
                return {"success": " Done insertion"}, 200
            except KeyError as k:
                print(k)
                return {'error': 'An error has occurred during this operation. {}'.format(k)}, 500

    @celery.task
    def paginate_requested_data(self, url_link):
        """
        get paginated data
        @param url_link:
        @return: None
        """
        self.make_request(url_link, redis_db)
