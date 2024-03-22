import pickle
from flask import current_app as app
from crypto.Cipher import Cipher

users_file = 'users.pickle'
users = {}

def load_users():
    """Loads users from a file."""
    global users
    try:
        with open(users_file, 'rb') as f:
            users = pickle.load(f)
    except FileNotFoundError:
        users = {}
        app.logger.info("Users file not found. Starting with an empty dictionary.")

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
    else:
        return users

def update_user_password(username, new_password):
    """Updates the password for a specific user."""
    user = get_users(username)
    if user:
        users[username]['password'] = encrypt_password(new_password)
        save_users()
        return True
    return False

def check_password(username, password):
    """Checks if the provided password matches the stored password."""
    user = get_users(username)
    if user:
        decrypted_password = decrypt_password(user['password'])
        print(f"Debug: Comparing input password [{password}] with decrypted stored password [{decrypted_password}]")
        # Check if the decrypted password matches the input password
        password_match = password == decrypted_password
        print(f"Debug: Password match status: {password_match}")
        return password_match
    return False

def encrypt_password(password):
    """Encrypts a plaintext password."""
    cipher = Cipher()
    return cipher.encrypt(password)

def decrypt_password(encrypted_password):
    """Decrypts an encrypted password."""
    cipher = Cipher()
    return cipher.decrypt(encrypted_password)

def all_users():
    """
    Returns all user data.

    :return: A dictionary containing all users.
    """
    return users

# Load users at application start
load_users()
