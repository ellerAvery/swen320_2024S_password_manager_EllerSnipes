# user_management.py
import pickle
from flask import current_app as app, session
from crypto.Cipher import Cipher

# Path to the users data file
users_file = 'users.pickle'

# Attempt to load existing users from the file or initialize an empty dict
try:
    with open(users_file, 'rb') as f:
        users = pickle.load(f)
except FileNotFoundError:
    users = {}

# Initialize the cipher for password encryption and decryption
cipher = Cipher()

def encrypt_password(password):
    """Encrypt a plaintext password."""
    return cipher.encrypt(password)

def decrypt_password(encrypted_password):
    """Decrypt an encrypted password."""
    return cipher.decrypt(encrypted_password)

def load_users():
    """Load users from a pickle file."""
    global users
    try:
        with open(users_file, 'rb') as f:
            users = pickle.load(f)
    except FileNotFoundError:
        app.logger.info("No users file found. Starting with an empty user base.")
        users = {}

def save_users():
    """Save the current users to a pickle file."""
    with open(users_file, 'wb') as f:
        pickle.dump(users, f)

def add_users(username, password, token):
    """Adds a new user if the username does not already exist."""
    global users  # Ensure users is accessible globally
    print(f"Attempting to add user: Username={username}, Password={password}, Token={token}")

    # Validate input parameters
    if len(username) < 5 or len(username) > 10:
        print("Error: Username must be between 5 and 10 characters long.")
        return False
    if len(password) < 8 or len(password) > 20:
        print("Error: Password must be between 8 and 20 characters long.")
        return False
    if len(token) < 10 or len(token) > 30:
        print("Error: Token must be between 10 and 30 characters long.")
        return False

    # Check for existing user
    if username in users:
        print(f"Error: User '{username}' already exists.")
        return False

    # Add the new user
    try:
        encrypted_password = encrypt_password(password)
        users[username] = {'password': encrypted_password, 'token': token}
        print(f"User '{username}' added successfully.")
        return True
    except Exception as e:
        print(f"Error adding user '{username}': {e}")
        return False

def save_encrypted_password(encrypted_password, token):
    if 'encrypted_passwords' not in session:
        session['encrypted_passwords'] = []
    
    session['encrypted_passwords'].append({'password': encrypted_password, 'key': token})
    session.modified = True

def get_user_token(username):
    """Retrieve the token for a given username."""
    user = get_users(username)  # Assuming this returns None if the user doesn't exist
    if user:
        return user.get('token')  # Assuming 'token' is the key where the token is stored
    else:
        return None  # Or raise an exception, depending on how you want to handle this case

def get_users(username=None):
    """Get a single user by username or all users if no username is specified."""
    if username:
        return users.get(username)
    else:
        return users

def update_user_password(username, new_password):
    """Update the password for a specific user."""
    if username in users:
        users[username]['password'] = encrypt_password(new_password)
        save_users()
        return True
    return False

def check_password(username, password):
    """Check if the provided password matches the stored encrypted password."""
    user = get_users(username)
    if user and decrypt_password(user['password']) == password:
        return True
    return False

def all_users():
    """Return all user data."""
    return users

# Ensure users are loaded when this module is imported
load_users()
