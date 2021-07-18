from flask import url_for
from flask_testing import TestCase
import requests_mock 
from unittest.mock import patch

from application import app, db
from application.models import Story

class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI = "sqlite:///data.db")
        return app

    def setUp(self):
        db.create_all()
        db.session.add(Story(character="Ricky", background="Young rich kid that grew up in the city", endpoint="Bad Ending"))
        db.session.commit 

    def tearDown(self):
        db.session.remove()

class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for("home"))
        self.assertEqual(response.status_code, 500)

class TestResponse(TestBase):
    def test_Ricky(self):
        with requests_mock.mock() as test:
            test.get("http://character_api:5001/get_character", text = 'Ricky')
            test.get("http://background_api:5002/get_background", text = 'Young rich kid that grew up in the city')
            test.post("http://endpoint_api:5003/get_endpoint", json = 'Bad Ending')
            response= self.client.get(url_for('home'))
            self.assertIn(b'Ricky', response.data)
            self.assertIn(b'Young rich kid that grew up in the city', response.data)
            self.assertIn(b'Bad Ending', response.data)

    def test_Ricky2(self):
        with requests_mock.mock() as test:
            test.get("http://character_api:5001/get_character", text = 'Ricky')
            test.get("http://background_api:5002/get_background", text = 'Young poor kid that grew up in the city')
            test.post("http://endpoint_api:5003/get_endpoint", json = 'Good Ending')
            response= self.client.get(url_for('home'))
            self.assertIn(b'Ricky', response.data)
            self.assertIn(b'Young poor kid that grew up in the city', response.data)
            self.assertIn(b'Good Ending', response.data)

    def test_Arian(self):
        with requests_mock.mock() as test:
            test.get("http://character_api:5001/get_character", text = 'Arian')
            test.get("http://background_api:5002/get_background", text = 'Young rich kid that grew up in the city')
            test.post("http://endpoint_api:5003/get_endpoint", json = 'Bad Ending')
            response= self.client.get(url_for('home'))
            self.assertIn(b'Arian', response.data)
            self.assertIn(b'Young rich kid that grew up in the city', response.data)
            self.assertIn(b'Bad Ending', response.data)

    def test_Arian2(self):
        with requests_mock.mock() as test:
            test.get("http://character_api:5001/get_character", text = 'Arian')
            test.get("http://background_api:5002/get_background", text = 'Young poor kid that grew up in the city')
            test.post("http://endpoint_api:5003/get_endpoint", json = 'Good Ending')
            response= self.client.get(url_for('home'))
            self.assertIn(b'Arian', response.data)
            self.assertIn(b'Young poor kid that grew up in the city', response.data)
            self.assertIn(b'Good Ending', response.data)
        
    def test_Thiago(self):
        with requests_mock.mock() as test:
            test.get("http://character_api:5001/get_character", text = 'Thiago')
            test.get("http://background_api:5002/get_background", text = 'Young rich kid that grew up in the city')
            test.post("http://endpoint_api:5003/get_endpoint", json = 'Good Ending')
            response= self.client.get(url_for('home'))
            self.assertIn(b'Thiago', response.data)
            self.assertIn(b'Young rich kid that grew up in the city', response.data)
            self.assertIn(b'Good Ending', response.data)

    def test_Thiago2(self):
        with requests_mock.mock() as test:
            test.get("http://character_api:5001/get_character", text = 'Thiago')
            test.get("http://background_api:5002/get_background", text = 'Young poor kid that grew up in the city')
            test.post("http://endpoint_api:5003/get_endpoint", json = 'Bad Ending')
            response= self.client.get(url_for('home'))
            self.assertIn(b'Thiago', response.data)
            self.assertIn(b'Young poor kid that grew up in the city', response.data)
            self.assertIn(b'Bad Ending', response.data)

    def test_Carson(self):
        with requests_mock.mock() as test:
            test.get("http://character_api:5001/get_character", text = 'Carson')
            test.get("http://background_api:5002/get_background", text = 'Young rich kid that grew up in the city')
            test.post("http://endpoint_api:5003/get_endpoint", json = 'Good Ending')
            response= self.client.get(url_for('home'))
            self.assertIn(b'Carson', response.data)
            self.assertIn(b'Young rich kid that grew up in the city', response.data)
            self.assertIn(b'Good Ending', response.data)

    def test_Carson2(self):
        with requests_mock.mock() as test:
            test.get("http://character_api:5001/get_character", text = 'Carson')
            test.get("http://background_api:5002/get_background", text = 'Young poor kid that grew up in the city')
            test.post("http://endpoint_api:5003/get_endpoint", json = 'Good Ending')
            response= self.client.get(url_for('home'))
            self.assertIn(b'Carson', response.data)
            self.assertIn(b'Young poor kid that grew up in the city', response.data)
            self.assertIn(b'Good Ending', response.data)

    def test_Duncan(self):
        with requests_mock.mock() as test:
            test.get("http://character_api:5001/get_character", text = 'Duncan')
            test.get("http://background_api:5002/get_background", text = 'Young rich kid that grew up in the city')
            test.post("http://endpoint_api:5003/get_endpoint", json = 'Bad Ending')
            response= self.client.get(url_for('home'))
            self.assertIn(b'Duncan', response.data)
            self.assertIn(b'Young rich kid that grew up in the city', response.data)
            self.assertIn(b'Bad Ending', response.data)

    def test_Duncan2(self):
        with requests_mock.mock() as test:
            test.get("http://character_api:5001/get_character", text = 'Duncan')
            test.get("http://background_api:5002/get_background", text = 'Young poor kid that grew up in the city')
            test.post("http://endpoint_api:5003/get_endpoint", json = 'Good Ending')
            response= self.client.get(url_for('home'))
            self.assertIn(b'Duncan', response.data)
            self.assertIn(b'Young poor kid that grew up in the city', response.data)
            self.assertIn(b'Good Ending', response.data)
