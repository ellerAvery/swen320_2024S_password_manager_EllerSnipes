import logging
from logging.handlers import RotatingFileHandler
from decouple import config
from flask import Flask
from flask_login import LoginManager

# Initialize Flask app
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

# Import user management functions
from .user_management import load_users

# Register Flask-Login user loader callback using user_management functions
@login_manager.user_loader
def user_loader(user_id):
    return load_users(user_id)

# Register blueprints
from .accounts.views import accounts_bp
from .core.views import core_bp

app.register_blueprint(accounts_bp)
app.register_blueprint(core_bp)
