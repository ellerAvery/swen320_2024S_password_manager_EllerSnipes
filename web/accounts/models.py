from flask_login import UserMixin, login_manager
from web.user_management import get_users, check_password

class User(UserMixin):
    def __init__(self, username):
        user_info = get_users(username)
        if user_info:
            self.username = username
            self.id = username  # Flask-Login uses this attribute to keep track of the user
            self.password_hash = user_info.get('password')

    @staticmethod
    def check_password(username, password):
        # Ideally, this should verify a password against a hashed version
        return check_password(username, password)

    @staticmethod
    def get(username):
        user_info = get_users(username)
        if user_info:
            return User(username)
        return None

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)
