from unittest import TestCase, mock
from unittest.mock import patch
from web.accounts.models import User
from web.user_management import get_users

class TestUser(TestCase):

    @mock.patch('web.user_management.get_users')
    def test_user_instantiation_existing_user(self, mock_get_users):
        mock_get_users.return_value = {'username': 'testuser', 'password': 'testpassword'}
        user = User('testuser')
        self.assertEqual(User.username, 'testuser')
        self.assertEqual(User.password, 'testpassword')

    @mock.patch('web.user_management.get_users')
    def test_user_instantiation_nonexistent_user(self, mock_get_users):
        mock_get_users.return_value = None
        user = User('nonexistent')
        self.assertIsNone(user.id)

##Avery continue tests