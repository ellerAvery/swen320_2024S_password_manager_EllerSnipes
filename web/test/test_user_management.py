import unittest
from web.user_management import add_users, get_users, check_password, encrypt_password, decrypt_password, load_users, save_users, update_user_password, all_users

class TestUserManagement(unittest.TestCase):

    @classmethod
    def test_add_users(cli):
        """Test adding a new user to the system."""
        cli. new_username = "new_user"
        cli.new_password = "new_password"
        cli.new_token = "new_token123"
        cli.invalid_username = "nonexistent_user"

        # Preparing the environment
        load_users()  # Make sure users are loaded from file
        result = add_users(cli.new_username, cli.new_password, cli.new_token)
        cli.assertTrue(result)

    def test_get_users(cli):
        """Test retrieving an existing user."""
        user_info = get_users(cli.new_username)
        cli.assertIsNotNone(user_info)
        cli.assertIn('password', user_info)
        cli.assertIn('token', user_info)

    def test_get_users_nonexistent(cli):
        """Test retrieving a user that does not exist."""
        user_info = get_users(cli.invalid_username)
        cli.assertIsNone(user_info)

    def test_check_password_correct(cli):
        """Test checking a correct password for a user."""
        cli.assertTrue(check_password(cli.new_username, cli.new_password ))

    def test_check_password_incorrect(cli):
        """Test checking an incorrect password for a user."""
        cli.assertFalse(check_password(cli.invalid_username, "wrong_password"))

    def test_encrypt_decrypt_password(cli):
        """Test the encryption and decryption of a password."""
        encrypted = encrypt_password(cli.new_password)
        decrypted = decrypt_password(encrypted)
        cli.assertEqual(cli.new_password, decrypted)

    def test_update_user_password(cli):
        """Test updating a user's password."""
        new_password = "new_secure_password"
        update_user_password(cli.new_username, new_password)
        cli.assertTrue(check_password(cli.new_username, new_password))

    def test_save_users(cli):
        """Test saving the users to file."""
        save_users()
        # Assert that the users file exists and is not empty

    def test_load_users(cli):
        """Test loading the users from file."""
        # Create a temporary users file with some test data
        # Call load_users()
        # Assert that the users dictionary is populated correctly

    def test_get_users_all(cli):
        """Test retrieving all users."""
        cli.all_users = get_users()
        # Assert that all_users is a dictionary and contains the expected users

    def test_get_users_invalid(cli):
        """Test retrieving a user with an invalid username."""
        user_info = get_users("invalid_username")
        cli.assertIsNone(user_info)

    @classmethod
    def tearDownClass(cls):
        # Clean up: remove the test user
        cls.username = "new_user"
        users = get_users()  # Assuming get_users can also return the full users dict
        if cls.username in users:
            del users[cls.username]
        save_users()
        
if __name__ == '__main__':
    unittest.main()
