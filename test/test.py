import unittest
from web import app

testUser = User()
testUser.__init__(self, 'test', 'password', 'testPassKey')

class TestLogin(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_loginSuccessful(self):
        response = self.app.post('/login', data=dict(username='test_user', password='password'), follow_redirects=True)

        self.assertEqual(response.status_code, 200)

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
    