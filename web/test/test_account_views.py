from unittest import TestCase
from unittest.mock import patch
from flask import Flask
from web.accounts.views import accounts_bp
from web.accounts.models import User

class TestViews(TestCase):

    def setUp(self):
        self.app = Flask(__name__,  template_folder='web/templates')
        self.app.config['SECRET_KEY'] = 'fejwifaosdIEWJFnfiwefnowe'

        self.app.register_blueprint(accounts_bp)
        self.client = self.app.test_client()

    @patch('web.accounts.views.get_users')
    @patch('web.accounts.views.add_users')
    def test_register_new_user(self, mock_add_users, mock_get_users):
        mock_get_users.return_value = None
        mock_add_users.return_value = True
        response = self.client.post('/register', data={'username': 'newuser', 'password': 'vpassword', 'token': 'validtoken123'})
        
        self.assertEqual(response.status_code, 200)
        # Check for successful registration response
        # This assumes you're redirecting or responding in a specific way on success
        

    def test_logout(self):
    # Simulate login possibly required before logout depending on implementation
        with self.client:
            self.client.post('/login', data={'username': 'testuser', 'password': 'testpass'})
            response = self.client.get('/logout')  # Ensure this is the correct method
            self.assertEqual(response.status_code, 302)  # Assuming redirect to login page
            self.assertTrue('location' in response.headers and 'login' in response.headers['location'])



##Avery continue tests