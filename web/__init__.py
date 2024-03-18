from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config

from .extensions import db, login_manager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from .accounts.views import accounts_bp
    app.register_blueprint(accounts_bp, url_prefix='/accounts')

    return app

