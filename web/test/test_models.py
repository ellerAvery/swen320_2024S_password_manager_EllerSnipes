from unittest import TestCase
from unittest.mock import patch
from web.accounts.models import User
from web.user_management import get_users

class TestUser(TestCase):

    @patch('web.user_management.get_users')
    def test_user_instantiation_existing_user(self, mock_get_users):
        mock_get_users.return_value = {'username': 'testuser'}
        user = User('testuser')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.password, 'testpassword')

    @patch('web.user_management.get_users')
    def test_user_instantiation_nonexistent_user(self, mock_get_users):
        mock_get_users.return_value = None
        user = User('nonexistent')
        self.assertIsNone(user.id)
