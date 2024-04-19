from unittest import TestCase
from unittest.mock import patch
import unittest
from flask_login import UserMixin
from web.accounts.models import User
from web.user_management import check_password, get_users

class TestUser(unittest.TestCase):
    @patch('web.accounts.models.get_users')
    def test_user_instantiation_existing_user(self, mock_get_users):
        mock_get_users.return_value = [{'username': 'testuser', 'password': 'testpassword'}]
        user = User('testuser')
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.is_authenticated)
        mock_get_users.assert_called_once_with()
    if __name__ == '__main__':
        unittest.main()