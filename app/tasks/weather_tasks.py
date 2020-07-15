import json
import os
import time
from datetime import datetime

import requests as req
from flask_sqlalchemy import SQLAlchemy

from app import app
from app.app import application
from app.extensions import celery
from app.model.weather_model import WeatherForecast
from app.utils.api_weather import url

db = SQLAlchemy(application)

# Add periodic tasks
celery_beat_schedule = {
    "time_scheduler": {
        "task": "app.tasks.weather_tasks.make_request",
        # Run every second
        "schedule": 30.0,
    }
}
# configure celery
celery.conf.update(
    result_backend=os.environ['REDIS_URL'],
    broker_url=os.environ['REDIS_URL'],
    timezone="UTC",
    task_serializer="json",
    accept_content=["json"],
    result_serializer="json",
    beat_schedule=celery_beat_schedule,
)


@celery.task
def make_request():
    """
    Make request to the url
    """

    # clear the table first, before adding new data.

    db.session.execute('''TRUNCATE TABLE weather_forecasts''')
    db.session.commit()
    db.session.close()

    filename = os.path.join(app.create_app().static_folder, 'data', 'current_city_list.json')
    with open(filename) as weather_file:
        data = json.load(weather_file)

    for i in data:

        lat = i['coord']['lat']
        lon = i['coord']['lon']
        name = i['name']

        res = req.get(
            'https://{url}?lat={lat}&lon={lon}&appid={api_key}'.format(url=url, lat=lat, lon=lon,
                                                                       api_key=os.environ['WEATHER_API_KEY']))

        for i in res.json()['list']:
            weather_type = i['weather'][0]['main']
            date_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(i['dt'])))
            date_time_obj = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
            description = i['weather'][0]['description']
            weather = WeatherForecast(weather_type=weather_type,
                                      date_time=date_time_obj,
                                      description=description,
                                      name=name,
                                      latitude=lat,
                                      longitude=lon
                                      )
            db.session.add(weather)
            db.session.commit()

    return "DONE"
