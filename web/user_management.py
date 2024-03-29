import pickle
from flask import current_app as app
from crypto.Cipher import Cipher

users_file = 'users.pickle'
users = {}

# Initialize the cipher once and use it for encryption and decryption
cipher = Cipher()

def encrypt_password(password):
    """Encrypts a plaintext password."""
    return cipher.encrypt(password)

def decrypt_password(encrypted_password):
    """Decrypts an encrypted password."""
    return cipher.decrypt(encrypted_password)

def load_users():
    """Loads users from a file, initializing with an empty dict if not found."""
    global users
    try:
        with open(users_file, 'rb') as f:
            users = pickle.load(f)
    except FileNotFoundError:
        users = {}
        # Use Flask's logging for consistency
        app.logger.info("Users file not found. Initialized with an empty dictionary.")

def save_users():
    """Saves the current users to a file."""
    with open(users_file, 'wb') as f:
        pickle.dump(users, f)

def add_users(username, password, token):
    """Adds a new user if the username does not already exist."""
    if username in users:
        return False  # User already exists
    users[username] = {'password': encrypt_password(password), 'token': token}
    save_users()
    return True

def get_users(username=None):
    """Returns information for a specific user, or all users if no username is provided."""
    if username:
        return users.get(username)
    return users

def update_user_password(username, new_password):
    """Updates the password for a specific user."""
    if username in users:
        users[username]['password'] = encrypt_password(new_password)
        save_users()
        return True
    return False

def check_password(username, password):
    """Checks if the provided password matches the stored password for a user."""
    if username not in users:
        return False
    decrypted_password = decrypt_password(users[username]['password'])
    return decrypted_password == password

def all_users():
    """Returns all user data."""
    return users

# Example usage should be removed or commented out to prevent execution during import
# if __name__ == "__main__":
#     load_users()
#     print("Adding user:", add_users("testuser", "password123", "token123"))
#     print("Getting user:", get_users("testuser"))
#     print("Checking password:", check_password("testuser", "password123"))
#     print("Updating password:", update_user_password("testuser", "newpassword"))
#     print("Checking updated password:", check_password("testuser", "newpassword"))
#     print("All users:", all_users())
