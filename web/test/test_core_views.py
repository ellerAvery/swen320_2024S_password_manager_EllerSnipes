from unittest import TestCase
from unittest.mock import patch
from flask import Flask
from web.core.views import core_bp
from crypto.Cipher import Cipher
from flask_login import login_required
from flask_login import LoginManager
cipher = Cipher()

class TestViews(TestCase):
    def setUp(self):
        self.app = Flask(__name__,  template_folder='templates')
        self.app.config['SECRET_KEY'] = 'fejwifaosdIEWJFnfiwefnowe'
        
        self.app.register_blueprint(core_bp)
        self.client = self.app.test_client()

    ''' def test_decrypt(self):
        password = cipher.encrypt("password")

        response = self.client.post('/decrypt', data={'passwordTextD': password})

        self.assertEqual(response, "password")

    def test_save_encrypted_passwords(self):
        password = "savePassword"
        response = self.client.post('/saveEncryptedPassword', data={'passwordTextD': password}) '''