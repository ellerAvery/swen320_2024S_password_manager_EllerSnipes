from unittest import TestCase
from crypto.Cipher import Cipher

cipher = Cipher()

class TestUserManagement(TestCase):

    def test_Encrypt(self):
        input = "test"
        result = cipher.encrypt("test")

        self.assertNotEqual(result, input)
        self.assertEqual(cipher.decrypt(result), input)

    