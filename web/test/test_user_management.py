import unittest
from web.accounts.models import User, UserMixin
from web.user_management import add_users, get_users, check_password, encrypt_password, decrypt_password, load_users, save_users, update_user_password, all_users
import pickle

class TestUserManagement(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Class level setup for the test cases."""
        # Ensure we're starting with a known state
        cls.initial_users = {
            "existing_user": {
                "password": encrypt_password("secure123"),
                "token": "token456"
            }
        }
        with open('users.pickle', 'wb') as f:
            pickle.dump(cls.initial_users, f)
        
        # Load the users from the file
        load_users()

    def setUp(self):
        """Set up test variables."""
        self.new_username = "testuser"
        self.new_password = "testpass"
        self.new_token = "testtoken"
        load_users()  # Reload users from the initial state

    def test_add_users(self):
        """Ensure a new user can be added."""
        # Ensure the users dictionary is in the expected state before testing
        #print("Before adding user:", all_users())

        # Attempt to add a new user
        result = add_users(self.new_username, self.new_password, self.new_token)
        self.assertTrue(result, "Expected True return value from add_users indicating success.")

        # Debugging: Check the state of users after attempting to add
        #print("After adding user:", all_users())

        # Assert the new user is present in the users dictionary
        self.assertIn(self.new_username, all_users(), "New user should be in users dictionary")

        # Optionally, confirm the details of the added user
        added_user = get_users(self.new_username)
        self.assertIsNotNone(added_user, "Added user details should be retrievable.")
        self.assertEqual(added_user['token'], self.new_token, "Token should match what was added.")

        # Debugging: Print the keys of the users dictionary after assertion
        #print("Keys in users dictionary after assertion:", all_users().keys())

    def test_get_users(self):
        """Ensure we can retrieve an existing user."""
        user_info = get_users("existing_user")
        self.assertIsNotNone(user_info)
        self.assertIn('password', user_info)
        self.assertIn('token', user_info)
        self.assertTrue(check_password("existing_user", "secure123"))

    def test_update_user_password(self):
        """Ensure we can update a user's password."""
        new_password = "updatedpassword"
        update_user_password("existing_user", new_password)
        self.assertTrue(check_password("existing_user", new_password))

    def test_encrypt_decrypt_password(self):
        """Ensure that password encryption and decryption work."""
        encrypted = encrypt_password(self.new_password)
        decrypted = decrypt_password(encrypted)
        self.assertEqual(self.new_password, decrypted)

    @classmethod
    def tearDownClass(cls):
        """Clean up by resetting the users file to its initial state."""
        with open('users.pickle', 'wb') as f:
            pickle.dump(cls.initial_users, f)

    if __name__ == '__main__':
        unittest.main()
    
'''          
    def test_save_users(self):
        """Ensure that users are saved correctly."""
        # Create a temporary users dictionary
        temp_users = {
            "user1": {
                "password": encrypt_password("password1"),
                "token": "token1"
            },
            "user2": {
                "password": encrypt_password("password2"),
                "token": "token2"
            }
        }

        # Save the temporary users
        save_users(temp_users)

        # Load the users from the file
        load_users()

        # Assert that the loaded users match the temporary users
        self.assertEqual(all_users(), temp_users, "Loaded users should match the saved users")

    def test_check_password(self):
        """Ensure that password checking works correctly."""
        # Add a new user
        add_users("testuser", "password123", "token123")

        # Check the password for the added user
        self.assertTrue(check_password("testuser", "password123"), "Password should match")

        # Check an incorrect password for the added user
        self.assertFalse(check_password("testuser", "incorrectpassword"), "Password should not match")

    def test_get_users_with_username(self):
        """Ensure that get_users returns the correct user when a username is provided."""
        # Add a new user
        add_users("testuser", "password123", "token123")

        # Get the details of the added user
        user_info = get_users("testuser")

        # Assert that the user details match the added user
        self.assertEqual(user_info["password"], encrypt_password("password123"), "Password should match")
        self.assertEqual(user_info["token"], "token123", "Token should match")

    def test_get_users_without_username(self):
        """Ensure that get_users returns all users when no username is provided."""
        # Add multiple users
        add_users("user1", "password1", "token1")
        add_users("user2", "password2", "token2")
        add_users("user3", "password3", "token3")

        # Get all users
        users_dict = get_users()

        # Assert that the number of users is correct
        self.assertEqual(len(users_dict), 4, "Number of users should be 4 (including the initial user)")

    def test_update_user_password_nonexistent_user(self):
        """Ensure that update_user_password returns False for a nonexistent user."""
        # Update the password for a nonexistent user
        result = update_user_password("nonexistent_user", "newpassword")

        # Assert that the result is False
        self.assertFalse(result, "Result should be False for a nonexistent user")

    def test_update_user_password_existing_user(self):
        """Ensure that update_user_password updates the password for an existing user."""
        # Add a new user
        add_users("testuser", "password123", "token123")

        # Update the password for the added user
        update_user_password("testuser", "newpassword")

        # Check the updated password for the added user
        self.assertTrue(check_password("testuser", "newpassword"), "Password should match the updated password")
'''
