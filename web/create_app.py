from flask import Flask
from flask_login import LoginManager
from decouple import config
import logging
from logging.handlers import RotatingFileHandler
from .accounts.models import User
from .accounts.views import accounts_bp
from .core.views import core_bp
from web.user_management import load_users
def create_app():
    app = Flask(__name__, template_folder='web/templates')
    app.config['SECRET_KEY'] = config('SECRET_KEY')
    app.config.from_object(config("APP_SETTINGS"))
    app.config['SERVER_NAME'] = '127.0.0.1:8080'
    app.config['APPLICATION_ROOT'] = '/'
    # Initialize Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "accounts.login"
    login_manager.login_message_category = "danger"

    # Register Blueprints
    app.register_blueprint(accounts_bp, url_prefix='/accounts')
    app.register_blueprint(core_bp)

    # Setup logging
    file_handler = RotatingFileHandler('application.log', maxBytes=10240, backupCount=10)
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.DEBUG)

    @login_manager.user_loader
    def load_users(user_id):
        return User.get(user_id)

    return app
