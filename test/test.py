import unittest
from web.accounts.forms import RegisterForm
from web.accounts.forms import passLenValid

class TestMethods(unittest.TestCase):
    def test_PassLenLower(self):
        inputForm = RegisterForm()
        inputPass = "1234"

        inputForm.password = inputPass
        
        self.assertFalse(passLenValid(inputForm))

    # def test_PassUpper(self):
    #     inputForm = RegisterForm
    #     inputPass = "123456789012345678901"

    #     inputForm.password = inputPass
    #     result = passLenValid(inputForm)

    #     self.assertFalse(result)