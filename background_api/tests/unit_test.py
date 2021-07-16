from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_background_api(self):
        for x in range(5):
            response = self.client.get(url_for('get_background'))
            backgrounds = [
                b'Young rich kid that grew up in the city',
                b'Young poor kid that grew up in the city', 
                ]
            self.assertIn(response.data, backgrounds)