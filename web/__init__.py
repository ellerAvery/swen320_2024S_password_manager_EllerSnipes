from flask import Flask
from flask_login import LoginManager, UserMixin
from decouple import config
import logging
from logging.handlers import RotatingFileHandler

from web.accounts.models import User
from .user_management import load_users, get_users  
from crypto.Cipher import Cipher 
app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))

# Setup logging
file_handler = RotatingFileHandler('application.log', maxBytes=10240, backupCount=10)
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.DEBUG)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "accounts.login"
login_manager.login_message_category = "danger"

# Define a user loader using a mock user class
@login_manager.user_loader
def user_loader(user_id):
    user_info = get_users(user_id)
    if user_info:
        user = User()  # Assuming you have a User class that extends UserMixin
        user.id = user_id
        return user
    return None

# Import and register blueprints after other imports to avoid circular dependencies
from .accounts.views import accounts_bp
from .core.views import core_bp

app.register_blueprint(accounts_bp)
app.register_blueprint(core_bp)
