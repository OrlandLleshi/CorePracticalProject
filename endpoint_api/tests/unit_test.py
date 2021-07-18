from flask import url_for
from flask_testing import TestCase
from unittest.mock import patch

from app import app

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_ricky1(self):
        response = self.client.get(url_for('endpoint'), json={'character':'Ricky', 'background':'Young rich kid that grew up in the city'})
        self.assertEqual(b'Bad Ending', response.data)

