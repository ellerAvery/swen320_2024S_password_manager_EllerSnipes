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
        self.new_token = "testtoken122shdcfbdh"
        load_users()  # Reload users from the initial state

    def test_add_users(self):
        """Ensure a new user can be added."""
        # Ensure the users dictionary is in the expected state before testing
        print("Before adding user:", all_users())

        # Attempt to add a new user
        result = add_users(self.new_username, self.new_password, self.new_token)
        self.assertTrue(result, "Expected True return value from add_users indicating success.")

        print("After adding user:", all_users())

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
        
    def test_add_user_with_short_password(self):
        """Ensure adding a user with a short password returns an error."""
        short_password = "short"
        result = add_users("testuser2", short_password, "validtoken")
        self.assertFalse(result, "Expected False due to short password.")

    def test_add_user_with_long_username(self):
        """Ensure adding a user with a long username returns an error."""
        long_username = "verylongusernameexceedinglimit"
        result = add_users(long_username, "validpassword", "validtoken")
        self.assertFalse(result, "Expected False due to long username.")

    def test_add_user_with_short_token(self):
        """Ensure adding a user with a short token returns an error."""
        short_token = "short"
        result = add_users("testuser3", "validpassword", short_token)
        self.assertFalse(result, "Expected False due to short token.")

    def test_retrieving_nonexistent_user(self):
        """Ensure that attempting to retrieve a nonexistent user returns None."""
        self.assertIsNone(get_users("nonexistent_user"), "Expected None for nonexistent user.")

    def test_retrieving_all_users(self):
        """Ensure that we can retrieve all users."""
        all_users_dict = all_users()
        self.assertIsInstance(all_users_dict, dict, "Expected all_users to return a dictionary.")
        self.assertIn("existing_user", all_users_dict, "Existing user should be in all users dictionary.")

    def test_adding_existing_user(self):
        """Ensure that adding a user with an existing username returns False."""
        result = add_users("existing_user", "newpassword", "newtoken")
        self.assertFalse(result, "Expected False when adding a user with an existing username.")


    @classmethod
    def tearDownClass(cls):
        """Clean up by resetting the users file to its initial state."""
        with open('users.pickle', 'wb') as f:
            pickle.dump(cls.initial_users, f)

    if __name__ == '__main__':
        unittest.main()
