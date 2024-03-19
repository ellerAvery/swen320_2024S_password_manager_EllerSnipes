from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import LoginManager, login_user, current_user, login_required, logout_user

from web.accounts.models import User
from .forms import LoginForm, RegisterForm, ChangePasswordForm
from user_management import add_user, get_user, update_user_password  # Assuming these functions exist
from crypto.Cipher import Cipher  # Check the correct import path

accounts_bp = Blueprint("accounts", __name__)

@accounts_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if add_user(form.username.data, form.password.data):
            flash('Registration successful!')
            return redirect(url_for('login'))
        else:
            flash('Registration failed. User may already exist.')
    return render_template('register.html', form=form)

@accounts_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        provided_password = form.password.data
        
        user_info = get_user(username)  # This should retrieve a user dict from your 'database'
        if user_info:
            cipher = Cipher()
            stored_password_encrypted = user_info['password']
            stored_password = cipher.decrypt(stored_password_encrypted)
            
            if provided_password == stored_password:
                user = User()  # Assuming User model conforms to Flask-Login's user mixin
                user.id = username  # Or however you choose to uniquely identify users
            
                # Flask-Login's login_user method to manage user session
                login_user(user)
                
                flash("Login successful!", "success")
                return redirect(url_for("core.home"))  # Adjust to your home page route
            else:
                flash("Invalid password, please try again.", "danger")
        else:
            flash("Username does not exist.", "danger")
    
    return render_template("login.html", form=form)

@LoginManager.user_loader
def load_user(user_id):
    user_info = get_user(user_id)  # Adjust if your user identification logic is different
    if user_info:
        user = User()  # User model conforming to Flask-Login's user mixin
        user.id = user_id
        return user
    return None

@accounts_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You were logged out.", "success")
    return redirect(url_for("accounts.login"))


@accounts_bp.route("/updatepass", methods=["GET", "POST"])
@login_required
def updatepass():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if update_user_password(current_user.get_id(), form.newPassword.data):  # Assuming this function exists
            flash("Password updated successfully!", "success")
        else:
            flash("User not found.", "danger")
    return render_template("accounts/updatepass.html", form=form)