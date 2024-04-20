import unittest
from unittest.mock import patch

from flask import Flask
from web.core.views import core_bp
from crypto.Cipher import Cipher
import json
from web.user_management import load_users, save_users, add_users, get_users, update_user_password, check_password, all_users, get_user_token

class TestEncryption(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__,  template_folder='templates')
        self.app.config['SECRET_KEY'] = 'fejwifaosdIEWJFnfiwefnowe'
        
        self.app.register_blueprint(core_bp)
        self.client = self.app.test_client()

    def test_encrypt_password(self):
        cipher = Cipher()
        password = "password"
        encrypted_password = cipher.encrypt(password)

        self.assertTrue(encrypted_password)
        self.assertNotEqual(password, encrypted_password)

    def test_decrypt_password(self):
        cipher = Cipher()
        password = "password"
        encrypted_password = cipher.encrypt(password)

        decrypted_password = cipher.decrypt(encrypted_password)

        self.assertEqual(password, decrypted_password)
        

class TestUsers(unittest.TestCase):

    @patch('web.user_management', 'test_users.json')
    def test_load_users_existing_file(self):
        users = {'user1': {'password': 'encrypted_password1', 'token': 'token127348392'}, 'user2': {'password': 'encrypted_password2', 'token': 'token27284945'}}
        with open('test_users.json', 'w') as f:
            json.dump(users, f)
        loaded_users = load_users()
        self.assertEqual(loaded_users, users)

    def test_load_users_non_existing_file(self):
        loaded_users = load_users()
        self.assertEqual(loaded_users, {})

    def test_save_users(self):
        users = {'user1': {'password': 'encrypted_password1', 'token': 'token1283744893'}, 'user2': {'password': 'encrypted_password2', 'token': 'hitdaclub247'}}
        save_users(users)
        with open('test_users.json', 'r') as f:
            saved_users = json.load(f)
        self.assertEqual(saved_users, users)

    def test_add_users_existing_username(self):
        add_users('user1', 'password1', 'token1283744893')
        self.assertEqual(get_users(), {})

    def test_add_users_non_existing_username(self):
        add_users('user1', 'password1', 'token1283744893')
        self.assertEqual(get_users(), {'user1': {'password': 'encrypted_password1', 'token': 'token1283744893'}})

    def test_update_user_password_existing_username(self):
        add_users('user1', 'password1', 'token138474292')
        update_user_password('user1', 'newerpassword')
        self.assertTrue(check_password('user1', 'newerpassword'))

    def test_update_user_password_non_existing_username(self):
        update_user_password('user1', 'newerpassword')
        self.assertEqual(get_users(), {})

    def test_check_password_existing_username(self):
        add_users('user1', 'password1', 'token12932934')
        self.assertTrue(check_password('user1', 'password1'))

    def test_check_password_non_existing_username(self):
        self.assertFalse(check_password('user1', 'password1'))

    def test_all_users(self):
        users = {'user12345': {'password': 'password12', 'token': 'token12345678910'}, 'user2': {'password': 'password2', 'token': 'tolkien12345'}}
        add_users('usher123', 'password1', 'token12345678910')
        add_users('llcoolj', 'password2', 'hitdaclub12345')
        self.assertEqual(all_users(), users)

    def test_get_user_token_existing_username(self):
        add_users('user1234', 'password1', 'token12345678910')
        self.assertEqual(get_user_token('user1234'), 'token12345678910')

    def test_get_user_token_non_existing_username(self):
        self.assertIsNone(get_user_token('user1'))