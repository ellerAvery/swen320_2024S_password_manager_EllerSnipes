import pickle
from flask import current_app as app
from crypto.Cipher import Cipher  # Assuming Cipher is correctly implemented

users_file = 'users.pickle'
users = {}

def load_users():
    global users
    try:
        with open(users_file, 'rb') as f:
            users = pickle.load(f)
    except FileNotFoundError:
        app.logger.info("Users file not found. Starting with an empty dictionary.")

def save_users():
    with open(users_file, 'wb') as f:
        pickle.dump(users, f)

def add_users(username, password):
    if username in users:
        return False  # User already exists
    cipher = Cipher()
    encrypted_password = cipher.encrypt(password)
    users[username] = {'password': encrypted_password}
    save_users()
    return True

def check_password(username, password):
    user = users.get(username)
    if not user:
        return False
    cipher = Cipher()
    return cipher.decrypt(user['password']) == password
def get_users(username):
    """
    Retrieve a user's information from the dictionary.
    
    :param username: The username of the user to retrieve.
    :return: The user's information if found, or None if not found.
    """
    # Assuming `users` is the global dictionary containing user data
    global users
    
    # Try to retrieve the user's information by username
    user_info = users.get(username)
    
    # Return the user's information if found, else return None
    return user_info if user_info else None

# Call load_users at application start
load_users()
