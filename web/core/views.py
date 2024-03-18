from flask import Blueprint, render_template
from flask_login import login_required

accounts_bp = Blueprint("core", __name__)

# Starts the Flask app
@accounts_bp.route('/')
@login_required
def home():
    return render_template("accounts/login.html")
