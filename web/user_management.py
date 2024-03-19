# user_management.py

import pickle
from flask import current_app as app
from crypto.Cipher import Cipher

# Initialize or load the user dictionary
def load_users():
    """Load the user dictionary from a file."""
    try:
        with open('users.pickle', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        app.logger.info("Users file not found. Starting with an empty dictionary.")
        return {}

def save_users(users_dict):
    """Save the user dictionary to a file."""
    with open('users.pickle', 'wb') as f:
        pickle.dump(users_dict, f)

def add_user(username, password, **kwargs):
    """Add a user to the dictionary with encrypted password."""
    users_dict = load_users()  # Define the users_dict variable
    cipher = Cipher()
    encrypted_password = cipher.encrypt(password)
    if username in users_dict:
        raise ValueError("User already exists.")
    users_dict[username] = {"password": encrypted_password, **kwargs}
    save_users(users_dict)
    
def get_user(username):
    """Retrieve a user's information."""
    users_dict = load_users()
    return users_dict.get(username, None)

def update_user(username, password):
    """Update a user's password."""
    users_dict = load_users()
    if username not in users_dict:
        return False  # User does not exist
    users_dict[username]['password'] = password
    save_users(users_dict)
    return True

def remove_user(username):
    """Remove a user from the dictionary."""
    users_dict = load_users()
    if username not in users_dict:
        return False  # User does not exist
    del users_dict[username]
    save_users(users_dict)
    return True
