from unittest import TestCase
from web.create_app import create_app

class TestCreateApp(TestCase):
    def test_create_app(self):
        testApp = create_app()

        self.assertTrue(testApp)