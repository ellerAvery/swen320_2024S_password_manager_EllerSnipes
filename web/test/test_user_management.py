import unittest
from web.user_management import add_users, get_users, check_password, encrypt_password, decrypt_password, load_users, save_users, update_user_password

class TestUserManagement(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.username = "test_user"
        cls.password = "secure_password"
        cls.token = "token123"
        cls.invalid_username = "nonexistent_user"

        # Preparing the environment
        load_users()  # Make sure users are loaded from file
        add_users(cls.username, cls.password, cls.token)  # Add a test user for fetching
    
    def test_add_users(self):
        """Test adding a new user to the system."""
        new_username = "new_user"
        new_password = "new_password"
        new_token = "new_token123"
        result = add_users(new_username, new_password, new_token)
        self.assertTrue(result)

    def test_get_users(self):
        """Test retrieving an existing user."""
        user_info = get_users(self.username)
        self.assertIsNotNone(user_info)
        self.assertIn('password', user_info)
        self.assertIn('token', user_info)

    def test_get_users_nonexistent(self):
        """Test retrieving a user that does not exist."""
        user_info = get_users(self.invalid_username)
        self.assertIsNone(user_info)

    def test_check_password_correct(self):
        """Test checking a correct password for a user."""
        self.assertTrue(check_password(self.username, self.password))

    def test_check_password_incorrect(self):
        """Test checking an incorrect password for a user."""
        self.assertFalse(check_password(self.username, "wrong_password"))

    def test_encrypt_decrypt_password(self):
        """Test the encryption and decryption of a password."""
        encrypted = encrypt_password(self.password)
        decrypted = decrypt_password(encrypted)
        self.assertEqual(self.password, decrypted)

    def test_update_user_password(self):
        """Test updating a user's password."""
        new_password = "new_secure_password"
        update_user_password(self.username, new_password)
        self.assertTrue(check_password(self.username, new_password))

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
        all_users = get_users()
        # Assert that all_users is a dictionary and contains the expected users

    def test_get_users_invalid(self):
        """Test retrieving a user with an invalid username."""
        user_info = get_users("invalid_username")
        self.assertIsNone(user_info)

    @classmethod
    def tearDownClass(cls):
        # Clean up: remove the test user
        users = get_users()  # Assuming get_users can also return the full users dict
        if cls.username in users:
            del users[cls.username]
        save_users()
        
if __name__ == '__main__':
    unittest.main()
