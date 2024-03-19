# user_manager.py

import pickle
from flask import current_app as app

# This dictionary will act as a simple database for users
# The structure will be: users_dict = {"username": {"password": "userpassword", "other_data": "data"}}
users_dict = {}

def load_users():
    """Load the user dictionary from a file."""
    try:
        with open('users.pickle', 'rb') as f:
            global users_dict
            users_dict = pickle.load(f)
    except FileNotFoundError:
        app.logger.info("Users file not found. Starting with an empty dictionary.")

def save_users():
    """Save the user dictionary to a file."""
    with open('users.pickle', 'wb') as f:
        pickle.dump(users_dict, f)

def add_user(username, password, **kwargs):
    """Add a user to the dictionary."""
    if username in users_dict:
        raise ValueError("User already exists.")
    users_dict[username] = {"password": password, **kwargs}
    save_users()

def get_user(username):
    """Retrieve a user's information."""
    return users_dict.get(username)

def update_user(username, password=None, **kwargs):
    """Update a user's information."""
    if username not in users_dict:
        raise ValueError("User does not exist.")
    if password:
        users_dict[username]['password'] = password
    users_dict[username].update(kwargs)
    save_users()

def remove_user(username):
    """Remove a user from the dictionary."""
    if username not in users_dict:
        raise ValueError("User does not exist.")
    del users_dict[username]
    save_users()
