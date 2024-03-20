import unittest
from web import app
from web.accounts.models import User
from web.accounts.forms import LoginForm, RegisterForm, ChangePasswordForm



class TestLogin(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_loginValidate(self):
        testForm = LoginForm(username = 'testname', password = 'password')

        self.assertTrue(testForm.validate())

    def test_loginValidateFail(self):
        testForm = LoginForm(username = 'testnametoolong', password = 'pass')

        self.assertFalse(testForm.validate())

    def test_loginSuccessful(self):
        response = self.app.post('/login', data=dict(username='test_user', password='password'), follow_redirects=True)

        self.assertTrue(response.validate())

    def test_loginFailure(self):
        response = self.app.post('/login', data=dict(username='test_user', password='wrong_password'), follow_redirects=True)
        
        self.assertNotEqual(response.status_code, 200)

class TestRegister(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_registerSuccessful(self):
        response = self.app.post('/register', data=dict(username='user', password='password', key = 'passKeyLong'), follow_redirects=True)
        
        self.assertEqual(response.status_code, 200)

    def test_registerFailure(self):
        response = self.app.post('/register', data=dict(username='user', password='pass', key = 'passKey'), follow_redirects=True)
        
        self.assertNotEqual(response.status_code, 200)
    