from tests import BaseTestCase


class TestsTours(BaseTestCase):

    def test_tours_submission_successfully(self):
        """Tests when the tour packages are submitted successfully"""
        with self.client:
            # get token after logging in.
            token = self.get_token()
            available_dates = [
                {
                    'date': "2018-05-05"
                },
                {
                    'date': "2018-07-07"
                }
            ]
            destinations = [
                {
                    'location': 'A',
                    'tour_type': 'Adventure',
                    "danger_type": 'Low'
                },
                {
                    'location': 'B',
                    'tour_type': 'Leisure',
                    'danger_type': 'Medium'
                }
            ]
            response = self.add_tour("London", "Its a nice tour", 30.0, available_dates, destinations, 30, token)
            self.assertEqual(response.status_code, 201)

    def test_get_all_tour_packages(self):
        """
        Get all tour packages
        :return:
        """
        with self.client:
            token = self.get_token()
            response = self.get_tour_packages(token)
            self.assertEqual(response.status_code, 200)

    def test_get_single_tour_package(self):
        """
        Get all tour packages
        :return:
        """
        with self.client:
            token = self.get_token()
            response = self.get_single_tour_package(1, token)
            self.assertEqual(response.status_code, 200)

    def test_update_single_tour_package(self):
        """
        update tour package
        :return:
        """

        with self.client:
            token = self.get_token()
            available_dates = [
                {
                    'date': "2010-05-05"
                },
                {
                    'date': "2018-07-07"
                }
            ]
            destinations = [
                {
                    'location': 'A',
                    'tour_type': 'Adventure',
                    "danger_type": 'Low'
                },
                {
                    'location': 'B',
                    'tour_type': 'Leisure',
                    'danger_type': 'Medium'
                }
            ]
            response = self.update_tour_package(1, "London 2", "Its amazing", 10.0, available_dates, destinations, 30,
                                                token)
            self.assertEqual(response.status_code, 200)

