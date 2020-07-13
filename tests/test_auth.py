import json
from datetime import datetime

from tests import BaseTestCase


class TestAuth(BaseTestCase):

    def test_successful_signup(self):
        """
        Test a user register's successfully.
        """
        with self.client:
            now = datetime.now()
            time = now.strftime("%H%M%S")
            res = self.register_user("ja{time}@gmail.com".format(time=time), "buki", "jau", "123456789")
            self.assertEqual(res.status_code, 201)

    def test_user_already_exists(self):
        """
        Test user already exists
        :return:
        """

        with self.client:
            self.register_user("jau@gmail.com", "buki", "jau", "123456789")
            res = self.register_user("jau@gmail.com", "buki", "jau", "123456789")
            self.assertEqual(res.status_code, 409)

    def test_user_login(self):
        """
        Test user logs in
        :return:
        """

        with self.client:
            self.register_user("jau20@gmail.com", "buki", "jau", "123456789")
            response = self.login_user("jau20@gmail.com", "123456789")
            self.assertEqual(response.status_code, 200)


