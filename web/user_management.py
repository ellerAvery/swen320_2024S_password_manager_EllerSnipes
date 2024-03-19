# Assuming this is part of your user_management.py module
import pickle
from crypto.Cipher import Cipher

# Initialize your users dictionary
users = {}

# Load users from a file
def load_users():
    global users
    try:
        with open('users.pickle', 'rb') as f:
            users = pickle.load(f)
    except FileNotFoundError:
        pass  # Handle the file not being found (e.g., first run)

# Save users to a file
def save_users():
    with open('users.pickle', 'wb') as f:
        pickle.dump(users, f)

# Add a new user
def add_user(username, password, token):
    cipher = Cipher()
    encrypted_password = cipher.encrypt(password)
    users[username] = {
        'password': encrypted_password,
        'token': token,
        # Any other user info here
    }
    save_users()

# Check if password matches for a user
def check_password(username, password):
    user = users.get(username)
    if user:
        cipher = Cipher()
        return cipher.decrypt(user['password']) == password
    return False

# Update a user's password
def set_password(username, new_password):
    if username in users:
        cipher = Cipher()
        encrypted_password = cipher.encrypt(new_password)
        users[username]['password'] = encrypted_password
        save_users()
        return True
    return False

# Encrypt a password (or any other text)
def encrypt_password(password, key):
    cipher = Cipher()
    return cipher.encrypt(password, key)

# Decrypt a password (or any other text)
def decrypt_password(encrypted_password):
    cipher = Cipher()
    return cipher.decrypt(encrypted_password)
