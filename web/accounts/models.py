from flask_login import UserMixin, login_manager
from web.user_management import get_users, check_password


class User(UserMixin):
    def __init__(self, username):
        user_info = get_users(username)
        if user_info:
            self.username = username
            self.id = username  # Flask-Login uses this attribute to keep track of the user
            self.password_hash = user_info.get('password')
            
    
    # Static method to check if the provided password matches the stored password for the given username
    @staticmethod
    def check_password(username, password):
        # Ideally, this should verify a password against a hashed version
        return check_password(username, password)
    
    # Static method to get a User object if the user exists
    @staticmethod 
    def get(username):
        # If the user exists, return a User object, otherwise return None
        user_info = get_users(username)
        if user_info:
            return User(username)
        return None
