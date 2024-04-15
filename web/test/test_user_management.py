import unittest
import json

from flask import Flask
from crypto.Cipher import Cipher
from create_app import accounts_bp, core_bp
from user_management import load_users, save_users, users, update_user_password, add_users, check_password, decrypt_password, encrypt_password, TOKEN_MAX_LEN, TOKEN_MIN_LEN, PASSWORD_MAX_LEN, PASSWORD_MIN_LEN, USERNAME_MAX_LEN, USERNAME_MIN_LEN

class TestUserManagement(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = 'fejwifaosdIEWJFnfiwefnowe'
        self.app.register_blueprint(accounts_bp)
        self.client = self.app.test_client()
        self.cipher = Cipher()

    def test_load_users(self):
        # Test loading users from an existing JSON file
        users_file = 'test_users.json'
        with open(users_file, 'w') as f:
            json.dump({'testuser': {'password': 'testpass', 'token': 'testtoken889293'}}, f)
        load_users()
        self.assertEqual(users, {'testuser': {'password': 'testpass', 'token': 'testtoken889293'}})

    def test_save_users(self):
        # Test saving users to a JSON file
        users['newuser'] = {'password': 'newerpass', 'token': 'newtoken123456'}
        save_users()
        with open('users.json', 'r') as f:
            loaded_users = json.load(f)
        self.assertEqual(loaded_users, users)

    def test_add_users_valid_input(self):
        # Test adding a new user with valid input
        users = {}
        add_users('newuser', 'newerpass', 'newertokening')
        self.assertEqual(users, {'newuser': {'password': 'newerpass', 'token': 'newertokening'}})

    def test_add_users_invalid_input(self):
        # Test adding a new user with invalid input
        users = {}
        self.assertFalse(add_users('newuser', 'newpass', 'newtoken1234567890dejkejdwfendnwekfr'))  # Token too long
        self.assertFalse(add_users('newuser1234567890', 'newpass', 'newtoken'))  # Username too long
        self.assertFalse(add_users('newuser', 'newpass', 'newertokening'))  # Password too short

    def test_update_user_password_valid_input(self):
        # Test updating a user's password with valid input
        users['existing_user'] = {'password': 'existingpass', 'token': 'existingtoken'}
        update_user_password('existing_user', 'newerpass')
        self.assertEqual(users['existing_user']['password'], 'newerpass')

    def test_update_user_password_invalid_input(self):
        # Test updating a user's password with invalid input
        users['existing_user'] = {'password': 'existingpass', 'token': 'existingtoken'}
        self.assertFalse(update_user_password('existing_user1234567890', 'newerpass'))  # Username too long

    def test_check_password_valid_input(self):
        # Test checking a user's password with valid input
        users['existing_user'] = {'password': 'existingpass', 'token': 'existingtoken'}
        self.assertTrue(check_password('existing_user', 'existingpass'))

    def test_check_password_invalid_input(self):
        # Test checking a user's password with invalid input
        users['existing_user'] = {'password': 'existingpass', 'token': 'existingtoken'}
        self.assertFalse(check_password('existing_user', 'wrongpass'))

    def tearDown(self):
        # Clean up by resetting the users file to its initial state
        with open('users.json', 'w') as f:
            json.dump({'existing_user': {'password': 'existingpass', 'token': 'existingtoken'}}, f)