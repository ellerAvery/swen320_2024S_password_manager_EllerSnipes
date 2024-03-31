import pickle
from flask import current_app as app
from crypto.Cipher import Cipher

users_file = 'users.pickle'
# Ensure that 'users' is initialized at the module level
try:
    with open(users_file, 'rb') as f:
        users = pickle.load(f)
except FileNotFoundError:
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
    global users  # Declare users as global
    try:
        with open(users_file, 'rb') as f:
            users = pickle.load(f)
    except FileNotFoundError:
        # Use Flask's logging for consistency
        app.logger.info("Users file not found. Initialized with an empty dictionary.")
        users = {}

def save_users(users):
    """Saves the current users to a file."""
    with open(users_file, 'wb') as f:
        pickle.dump(users, f)
    

def add_users(username, password, token):
    """Adds a new user if the username does not already exist."""
    global users  # Declare users as global
    print("Before adding user:", users)
    
    # Validate input (as an example, more thorough validation may be needed)
    if not username or not password or not token:
        print("Invalid input provided to add_users.")
        return False

    # Check for existing user
    if username in users:
        print(f"Attempted to add existing user: {username}")
        return False

    # Encrypt password and add new user
    try:
        encrypted_password = encrypt_password(password)
        users[username] = {'password': encrypted_password, 'token': token}
        save_users(users)
        print(f"User added successfully: {username}")
        print("After adding user:", users)  # Debug print
        return True
    except Exception as e:
        print(f"Error adding user {username}: {e}")
        return False

def get_users(username=None):
    """Returns information for a specific user, or all users if no username is provided."""
    if username:
        return users.get(username)
    return users

def update_user_password(username, new_password):
    """Updates the password for a specific user."""
    if username in users:
        users[username]['password'] = encrypt_password(new_password)
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
#print("All users:", all_users())
