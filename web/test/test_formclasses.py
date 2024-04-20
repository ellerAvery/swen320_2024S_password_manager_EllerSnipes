from unittest import TestCase
from unittest.mock import patch
from web.accounts.forms import RegisterForm
from web.user_management import get_users

class TestRegisterForm(TestCase):
    
    @patch('web.user_management.get_users')
    def test_username_already_registered(self, mock_get_users):
        mock_get_users.return_value = {'username': 'users1'}
        form = RegisterForm(data={'username': 'user1', 'password': 'encrypted_password1', 'token': 'token127348392'})
        self.assertFalse(form.validate())
        self.assertIn("Username already registered.", form.username.errors)

    @patch('web.user_management.get_users')
    def test_valid_registration(self, mock_get_users):
        mock_get_users.return_value = None
        form = RegisterForm(data={'username': 'newuser', 'password': 'vpassword', 'token': 'validtoken123'})
        self.assertTrue(form.validate())

    def test_invalid_password(self):
        form = RegisterForm(data={'username': 'newuser', 'password': 'pass', 'token': 'validtoken123'})
        self.assertFalse(form.validate())

    def test_invalid_token(self):
        form = RegisterForm(data={'username': 'newuser', 'password': 'validpassword123', 'token': 'token'})
        self.assertFalse(form.validate())

    def test_invalid_username(self):
        form = RegisterForm(data={'username': 'new', 'password': 'validpassword123', 'token': 'validtoken12345'})
        self.assertFalse(form.validate())
