from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_character_api(self):
        for x in range(5):
            response = self.client.get(url_for('get_character'))
            characters = [b'Arian',b'Ricky', b'Thiago',b'Carson',b'Duncan']
            self.assertIn(response.data, characters)