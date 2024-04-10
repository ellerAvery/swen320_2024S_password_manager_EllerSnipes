from unittest import TestCase
from unittest.mock import patch
from web.accounts.forms import RegisterForm

class TestRegisterForm(TestCase):
    
    @patch('web.accounts.forms.get_users')
    def test_username_already_registered(self, mock_get_users):
        mock_get_users.return_value = {'username': 'existinguser'}
        form = RegisterForm(data={'username': 'existinguser', 'password': 'validpassword123', 'token': 'validtoken1234567890'})
        self.assertFalse(form.validate())
        self.assertIn("Username already registered.", form.username.errors)

    @patch('web.accounts.forms.get_users')
    def test_valid_registration(self, mock_get_users):
        mock_get_users.return_value = None
        form = RegisterForm(data={'username': 'newuser', 'password': 'validpassword123', 'token': 'validtoken1234567890'})
        self.assertTrue(form.validate())

##Avery continue tests