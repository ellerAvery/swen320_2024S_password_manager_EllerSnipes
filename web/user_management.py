import pickle
from flask import current_app as app
from crypto.Cipher import Cipher

# Constants for the file path and user constraints
USERS_FILE = 'users.pickle'
USERNAME_MIN_LEN, USERNAME_MAX_LEN = 5, 10
PASSWORD_MIN_LEN, PASSWORD_MAX_LEN = 8, 20
TOKEN_MIN_LEN, TOKEN_MAX_LEN = 10, 30

# Global users dictionary
users = {}

# Initialize the cipher for password encryption and decryption
cipher = Cipher()

def load_users():
    """Load users from a pickle file or initialize as an empty dictionary if not found."""
    global users
    try:
        with open(USERS_FILE, 'rb') as f:
            users = pickle.load(f)
    except FileNotFoundError:
        app.logger.info("No users file found. Initializing an empty user base.")
        users = {}

def save_users():
    """Save the current users dictionary to a pickle file."""
    with open(USERS_FILE, 'wb') as f:
        pickle.dump(users, f)

def encrypt_password(password):
    """Encrypt a plaintext password."""
    return cipher.encrypt(password)

def decrypt_password(encrypted_password):
    """Decrypt an encrypted password."""
    return cipher.decrypt(encrypted_password)

def get_user_token(username):
    """Retrieve the token for a given username."""
    user = get_users(username)  # Assuming this returns None if the user doesn't exist
    if user:
        return user.get('token')  # Assuming 'token' is the key where the token is stored
    else:
        return None  # Or raise an exception, depending on how you want to handle this case


def add_users(username, password, token):
    """Attempt to add a new user if the username does not already exist."""
    # Validate input parameters
    if not (USERNAME_MIN_LEN <= len(username) <= USERNAME_MAX_LEN):
        app.logger.error(f"Username length error: {username}")
        return False
    if not (PASSWORD_MIN_LEN <= len(password) <= PASSWORD_MAX_LEN):
        app.logger.error("Password length error")
        return False
    if not (TOKEN_MIN_LEN <= len(token) <= TOKEN_MAX_LEN):
        app.logger.error("Token length error")
        return False

    # Check if the username already exists
    if username in users:
        app.logger.error(f"Attempt to add existing user: {username}")
        return False

    # Add new user with encrypted password
    try:
        users[username] = {'password': encrypt_password(password), 'token': token}
        save_users()  # Ensure data is saved to file
        app.logger.info(f"New user added: {username}")
        return True
    except Exception as e:
        app.logger.error(f"Failed to add user {username}: {e}")
        return False

def update_user_password(username, new_password):
    """Update the password for an existing user."""
    if username in users:
        users[username]['password'] = encrypt_password(new_password)
        save_users()
        return True
    app.logger.error(f"Password update failed: User {username} not found")
    return False

def check_password(username, password):
    """Verify if the provided password matches the stored password for a user."""
    user = users.get(username)
    if user and decrypt_password(user['password']) == password:
        return True
    return False

def get_users(username=None):
    """Retrieve user information by username, or all users if no username is provided."""
    if username:
        return users.get(username)
    return users

# Load user data from file on module import
load_users()
