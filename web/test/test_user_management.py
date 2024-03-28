import os
import pickle
import unittest
from web.user_management import add_users, get_users, check_password, encrypt_password, decrypt_password, load_users, save_users, update_user_password, all_users
from web.user_management import users

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
        

    def test_load_users(self):
        """Test loading the users from file."""
        # Create a temporary users file with some test data
        users_file = "users.pickle"  
        
        test_users = {
            "user1": {
                "password": "password1",
                "token": "token1"
            },
            "user2": {
                "password": "password2",
                "token": "token2"
            }
        }
        with open(users_file, "wb") as file:
            pickle.dump(test_users, file)

        # Call load_users()
        load_users()

        # Assert that the users dictionary is populated correctly
        self.assertEqual(users, test_users)

    def test_save_users(self):
        """Test saving the users to file."""
        # Create a temporary users dictionary
        test_users = {
            "user1": {
                "password": "password1",
                "token": "token1"
            },
            "user2": {
                "password": "password2",
                "token": "token2"
            }
        }
        users_file = "users.pickle"

        users.update(test_users)

        # Call save_users()
        save_users()

        # Assert that the users file exists and is not empty
        self.assertTrue(os.path.exists(users_file))
        self.assertGreater(os.path.getsize(users_file), 0)

    def test_add_users(self):
        """Test adding a new user to the system."""
        username = "new_user"
        password = "new_password"
        token = "new_token123"

        # Call add_users()
        result = add_users(username, password, token)

        # Assert that the user was added successfully
        self.assertTrue(result)
        self.assertIn(username, users)
        self.assertEqual(users[username]["password"], password)
        self.assertEqual(users[username]["token"], token)

    def test_get_users_all(self):
        """Test retrieving all users."""
        # Call get_users() without passing a username
        all_users = get_users()

        # Assert that all_users is a dictionary and contains the expected users
        self.assertIsInstance(all_users, dict)
        self.assertEqual(all_users, users)

    def test_get_users_invalid(self):
        """Test retrieving a user with an invalid username."""
        invalid_username = "invalid_username"

        # Call get_users() with an invalid username
        user_info = get_users(invalid_username)

        # Assert that the user_info is None
        self.assertIsNone(user_info)

    @classmethod
    def tearDownClass(cls):
        users = get_users()  # Assuming get_users can also return the full users dict
        if "new_user" in users:
            del users["new_user"]
        save_users()

if __name__ == '__main__':
    unittest.main()
