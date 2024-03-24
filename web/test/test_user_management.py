import unittest
from web.user_management import add_users, get_users, check_password, encrypt_password, decrypt_password, load_users, save_users, update_user_password, all_users

class TestUserManagement(unittest.TestCase):

    def setUp(self):
        """Set up test variables."""
        self.new_username = "new_user"
        self.new_password = "new_password"
        self.new_token = "new_token123"
        self.invalid_username = "nonexistent_user"
        load_users()  # Make sure users are loaded from file

    def test_add_users(self):
        """Test adding a new user to the system."""
        result = add_users(self.new_username, self.new_password, self.new_token)
        self.assertTrue(result)

    def test_get_users(self):
        """Test retrieving an existing user."""
        user_info = get_users(self.new_username)
        self.assertIsNotNone(user_info)
        self.assertIn('password', user_info)
        self.assertIn('token', user_info)

    def test_get_users_nonexistent(self):
        """Test retrieving a user that does not exist."""
        user_info = get_users(self.invalid_username)
        self.assertIsNone(user_info)

    def test_check_password_correct(self):
        """Test checking a correct password for a user."""
        self.assertTrue(check_password(self.new_username, self.new_password ))

    def test_check_password_incorrect(self):
        """Test checking an incorrect password for a user."""
        self.assertFalse(check_password(self.invalid_username, "wrong_password"))

    def test_encrypt_decrypt_password(self):
        """Test the encryption and decryption of a password."""
        encrypted = encrypt_password(self.new_password)
        decrypted = decrypt_password(encrypted)
        self.assertEqual(self.new_password, decrypted)

    def test_update_user_password(self):
        """Test updating a user's password."""
        new_password = "new_secure_password"
        update_user_password(self.new_username, new_password)
        self.assertTrue(check_password(self.new_username, new_password))

    def test_save_users(self):
        """Test saving the users to file."""
        save_users()
        # Assert that the users file exists and is not empty

    def test_load_users(self):
        """Test loading the users from file."""
        # Create a temporary users file with some test data
        # Call load_users()
        # Assert that the users dictionary is populated correctly

    def test_get_users_all(self):
        """Test retrieving all users."""
        self.all_users = get_users()
        # Assert that all_users is a dictionary and contains the expected users

    def test_get_users_invalid(self):
        """Test retrieving a user with an invalid username."""
        user_info = get_users("invalid_username")
        self.assertIsNone(user_info)

    @classmethod
    def tearDownClass(cls):
        users = get_users()  # Assuming get_users can also return the full users dict
        if "new_user" in users:
            del users["new_user"]
        save_users()

if __name__ == '__main__':
    unittest.main()
