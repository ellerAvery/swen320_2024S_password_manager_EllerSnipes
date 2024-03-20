import pickle
from flask import current_app as app
from crypto.Cipher import Cipher 
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

def add_users(username, password, token):
    if username in users:
        return False  # User already exists
    users[username] = {'password': encrypt_password(password), 'token': token}
    save_users()
    return True

def get_users(username):
    """Retrieve a user's information."""
    return users.get(username)

def update_user_password(username, new_password):
    """Update a user's password."""
    user = get_users(username)
    if user:
        users[username]['password'] = encrypt_password(new_password)
        save_users()
        return True
    return False

def check_password(username, password):
    """Check if the provided password matches the stored password."""
    user = get_users(username)
    if user:
        return password == decrypt_password(user['password'])
    return False

def encrypt_password(password):
    """Encrypt a plaintext password."""
    cipher = Cipher()
    return cipher.encrypt(password)

def decrypt_password(encrypted_password):
    """Decrypt an encrypted password."""
    cipher = Cipher()
    return cipher.decrypt(encrypted_password)

# Load users at application start
load_users()
