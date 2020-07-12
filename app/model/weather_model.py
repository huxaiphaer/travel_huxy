from app.extensions import db


class WeatherForecast(db.Model):
    __tablename__ = 'weather_forecasts'

    id = db.Column(db.Integer, primary_key=True)
    weather_type = db.Column(db.String(50))
    date_time = db.Column(db.DateTime)
    description = db.Column(db.String(50))
    latitude = db.Column(db.String(20))
    longitude = db.Column(db.String(20))
    name = db.Column(db.String(20))
