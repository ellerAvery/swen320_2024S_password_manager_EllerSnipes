from unittest import TestCase
from unittest.mock import patch
from flask import Flask
from web.accounts.views import accounts_bp

class TestViews(TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(accounts_bp)
        self.client = self.app.test_client()

    @patch('web.accounts.views.get_users')
    @patch('web.accounts.views.add_users')
    def test_register_new_user(self, mock_add_users, mock_get_users):
        mock_get_users.return_value = None
        mock_add_users.return_value = True
        response = self.client.post('/register', data={'username': 'newuser', 'password': 'validpassword123', 'token': 'validtoken1234567890'})
        # Check for successful registration response
        # This assumes you're redirecting or responding in a specific way on success
        
    @patch('web.accounts.views.get_users')
    def test_login_existing_user(self, mock_get_users):
        mock_get_users.return_value = {'username': 'existinguser', 'password': 'hashedpassword'}
        # You would need to mock check_password as well, assuming it verifies password correctness
        # Perform login request and verify response


##Avery continue tests