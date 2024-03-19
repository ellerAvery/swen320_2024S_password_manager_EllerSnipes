from flask_login import UserMixin
from user_management import get_user, check_password

class User(UserMixin):
    def __init__(self, username):
        user_info = get_user(username)
        if user_info:
            self.username = username
            self.id = username  # Flask-Login requires an `id` attribute but you can use `username`
            self.password_hash = user_info.get('password')

    @staticmethod
    def check_password(username, password):
        return check_password(username, password)

    @staticmethod
    def get(username):
        user_info = get_user(username)
        if user_info:
            return User(username)
        return None
