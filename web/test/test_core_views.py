from unittest import TestCase
from unittest.mock import patch
from flask import Flask
from web.core.views import core_bp
from crypto.Cipher import Cipher
from flask_login import login_required

cipher = Cipher()

class TestViews(TestCase):
    def setUp(self):
        self.app = Flask(__name__,  template_folder='templates')
        self.app.config['SECRET_KEY'] = 'fejwifaosdIEWJFnfiwefnowe'

        self.app.register_blueprint(core_bp)
        self.client = self.app.test_client()


    @patch('flask_login.login_required')
    def test_encrypt(self, mock_login_required):
        mock_login_required.returnValue = True

        password = "password"

        response = self.client.post('/encrypt', data={'passwordTextE': password})

        self.assertEqual(response, cipher.encrypt(password))

    def test_decrypt(self):
        password = cipher.encrypt("password")

        response = self.client.post('/decrypt', data={'passwordTextD': password})

        self.assertEqual(response, "password")

    def test_save_encrypted_passwords(self):
        password = "savePassword"
        response = self.client.post('/saveEncryptedPassword', data={'passwordTextD': password})