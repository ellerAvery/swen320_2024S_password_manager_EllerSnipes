from flask import Flask
from flask_login import LoginManager
from decouple import config
import logging
from logging.handlers import RotatingFileHandler
from web.accounts.models import User
from web.user_management import get_users
from web.accounts.views import accounts_bp
from web.core.views import core_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = config('SECRET_KEY')
# Load the configuration from the environment variable APP_SETTINGS
app.config.from_object(config("APP_SETTINGS"))

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "accounts.login"
login_manager.login_message_category = "danger"

@login_manager.user_loader
def user_loader(user_id):
    user_info = get_users(user_id)
    if user_info:
        user = User(username=user_id)
        user.id = user_id
        return user
    return None

# Register the blueprints
app.register_blueprint(accounts_bp, url_prefix='/accounts')
app.register_blueprint(core_bp)

# Setup logging
file_handler = RotatingFileHandler('application.log', maxBytes=10240, backupCount=10)
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.DEBUG)
