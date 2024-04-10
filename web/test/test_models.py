from unittest import TestCase, mock
from web.accounts.models import User

class TestUser(TestCase):

    @mock.patch('web.user_management.get_users')
    def test_user_instantiation_existing_user(self, mock_get_users):
        mock_get_users.return_value = {'username': 'testuser', 'password': 'testpassword'}
        user = User('testuser')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.password, 'testpassword')

    @mock.patch('web.user_management.get_users')
    def test_user_instantiation_nonexistent_user(self, mock_get_users):
        mock_get_users.return_value = None
        user = User('nonexistent')
        self.assertIsNone(user.id)

##Avery continue tests