from flask_login import UserMixin, login_manager
from web.user_management import get_users, check_password


class User(UserMixin):
    def __init__(self, username):
        user_info = get_users(username)
        if user_info:
            self.username = username
            self.id = username  # Flask-Login uses this attribute to keep track of the user.
            # Directly use the password from user_info if hashing is not considered.
            self.password = user_info.get('password')
        else:
            self.id = None
            
    
    # Static method to check if the provided password matches the stored password for the given username
    @staticmethod
    def check_password(username, password):
        return check_password(username, password)
    
    # Static method to get a User object if the user exists
    @staticmethod 
    def get(username):
        # If the user exists, return a User object, otherwise return None
        user_info = get_users(username)
        if user_info:
            return User(username)
        return None
