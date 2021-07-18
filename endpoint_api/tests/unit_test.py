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

    def test_ricky2(self):
        response = self.client.get(url_for('endpoint'), json={'character':'Ricky', 'background':'Young poor kid that grew up in the city'})
        self.assertEqual(b'Good Ending', response.data)

    def test_arian1(self):
        response = self.client.get(url_for('endpoint'), json={'character':'Arian', 'background': 'Young rich kid that grew up in the city'})
        self.assertEqual(b'Bad Ending', response.data)

    def test_arian2(self):
        response = self.client.get(url_for('endpoint'), json={'character':'Arian', 'background': 'Young poor kid that grew up in the city'})
        self.assertEqual(b'Good Ending', response.data)

    def test_thiago1(self):
        response= self.client.get(url_for('endpoint'), json={'character':'Thiago', 'background': 'Young rich kid that grew up in the city'})
        self.assertEqual(b'Good Ending', response.data)

    def test_thiago2(self):
        response= self.client.get(url_for('endpoint'), json={'character':'Thiago', 'background': 'Young poor kid that grew up in the city'})
        self.assertEqual(b'Bad Ending', response.data)

    def test_carson1(self):
        response=self.client.get(url_for('endpoint'), json={'character':'Carson', 'background': 'Young rich kid that grew up in the city'})
        self.assertEqual(b'Good Ending', response.data)

    def test_carson2(self):
        response=self.client.get(url_for('endpoint'), json={'character':'Carson', 'background': 'Young poor kid that grew up in the city'})
        self.assertEqual(b'Good Ending', response.data)

    def test_duncan1(self):
        response= self.client.get(url_for('endpoint'), json={'character':'Duncan', 'background':'Young rich kid that grew up in the city'})
        self.assertEqual(b'Bad Ending', response.data)

    def test_duncan2(self):
        response= self.client.get(url_for('endpoint'), json={'character':'Duncan', 'background':'Young poor kid that grew up in the city'})
        self.assertEqual(b'Good Ending', response.data)

    

