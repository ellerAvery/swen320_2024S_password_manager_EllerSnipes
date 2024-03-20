from flask import Flask
from flask_login import LoginManager
from decouple import config
import logging
from logging.handlers import RotatingFileHandler
from web.accounts.models import User, UserMixin, login_manager, load_user
from .user_management import load_users, get_users, save_users, add_users
from .accounts.views import accounts_bp
from .core.views import core_bp
# Create a new Flask application
app = Flask(__name__)
# Load the configuration from the environment variable APP_SETTINGS
app.config.from_object(config("APP_SETTINGS"))

# Setup logging
# Create a rotating file handler, which logs even debug messages
file_handler = RotatingFileHandler('application.log', maxBytes=10240, backupCount=10)
file_handler.setLevel(logging.DEBUG)
# Create a formatter and set it for the file handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
# Add the file handler to the app's logger
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.DEBUG)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
# Specify the view to redirect to when the user needs to log in.
login_manager.login_view = "accounts.login"
# Set the message category for the flash message warning the user to log in.
login_manager.login_message_category = "danger"

# Define a user loader using a mock user class
@login_manager.user_loader
def user_loader(user_id):
    """
    Load a user from the user_id.

    Args:
        user_id (str): The ID of the user to load.

    Returns:
        User or None: The loaded User object if the user exists, None otherwise.
    """
    user_info = get_users(user_id)
    if user_info:
        user = User()  # Assuming you have a User class that extends UserMixin
        user.id = user_id
        return user
    return None

# Register the blueprints
app.register_blueprint(accounts_bp)
app.register_blueprint(core_bp)
