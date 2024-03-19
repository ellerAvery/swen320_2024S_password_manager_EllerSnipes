import logging
from logging.handlers import RotatingFileHandler
from decouple import config
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))

# Create a file handler for logging
file_handler = RotatingFileHandler('application.log', maxBytes=10240, backupCount=10)
file_handler.setLevel(logging.DEBUG)

# Create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Add the file handler to the Flask app's logger
app.logger.addHandler(file_handler)

# Set the level for the app's logger
app.logger.setLevel(logging.DEBUG)

login_manager = LoginManager()
login_manager.init_app(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Blueprints
from web.accounts.views import accounts_bp
from web.core.views import core_bp

app.register_blueprint(accounts_bp)
app.register_blueprint(core_bp)

login_manager.login_view = "accounts.login"
login_manager.login_message_category = "danger"

from web.accounts.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == int(user_id)).first()