from tests import BaseTestCase


class WeatherTest(BaseTestCase):
    def add_weather_data(self):
        with self.client:
            token = self.get_token()
            response = self.get_weather_data("34.790878", "48.570728", token)
            self.assertEqual(response.status_code, 200)
