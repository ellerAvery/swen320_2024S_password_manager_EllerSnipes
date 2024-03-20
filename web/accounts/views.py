from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import logout_user, login_required, current_user, login_user

from web.accounts.models import User
from .forms import LoginForm, RegisterForm, ChangePasswordForm
from web.user_management import add_users, get_users, check_password, encrypt_password, decrypt_password


accounts_bp = Blueprint('accounts', __name__)

@accounts_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        success = add_users(form.username.data, form.password.data, form.token.data)
        if success:
            flash('Registration successful!', 'success')
            return redirect(url_for('accounts.login'))
        else:
            flash('User already exists.', 'danger')
    return render_template('register.html', form=form)

@accounts_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user_info = get_users(form.username.data)
        if user_info and check_password(form.username.data, form.password.data):
            # Create a user instance for Flask-Login
            user = User()  # This part needs to be adjusted based on your User class
            user.id = form.username.data  # Or any unique identifier for the User
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('core.encrypt'))
        else:
            flash('Invalid username or password.', 'danger')
    return render_template('login.html', form=form)  # Corrected the template path

@accounts_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('accounts.login'))

@accounts_bp.route('/update_password', methods=['GET', 'POST'])
@login_required
def update_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        user_info = get_users(current_user.username)
        if user_info and check_password(current_user.username, form.old_password.data):
            success = update_password(current_user.username, encrypt_password(form.new_password.data))
            if success:
                flash('Your password has been updated!', 'success')
                return redirect(url_for('accounts.login'))
            else:
                flash('There was an error updating your password.', 'danger')
        else:
            flash('Old password is incorrect.', 'danger')
    return render_template('updatepass.html', form=form)  # Corrected the template path
