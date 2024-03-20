from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import LoginManager, login_user, current_user, login_required, logout_user
from crypto.Cipher import Cipher
from user_management import add_user, get_user, save_users, check_password
from .forms import LoginForm, RegisterForm, ChangePasswordForm  

accounts_bp = Blueprint('accounts', __name__)

@accounts_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        success = add_user(form.username.data, form.password.data, form.token.data)
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
        user_info = get_user(form.username.data)
        if user_info and check_password(form.username.data, form.password.data):
            # Implement login logic here, possibly using Flask-Login
            flash('Login successful!', 'success')
            return redirect(url_for('core.encrypt'))
        else:
            flash('Invalid username or password.', 'danger')
    return render_template('login.html', form=form)

@accounts_bp.route('/logout')
@login_required
def logout():
    logout_user()  # Flask-Login's logout_user method to end the user session
    flash('You have been logged out.', 'info')
    return redirect(url_for('accounts.login'))

@accounts_bp.route('/update_password', methods=['GET', 'POST'])
@login_required
def update_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        user_info = get_user(current_user.username)  # Assuming `current_user` is managed by Flask-Login and contains the username
        if Cipher().check_password(form.old_password.data, user_info['password']):  # Assuming a method to check password in Cipher class
            success = update_password(current_user.username, Cipher().encrypt(form.new_password.data))  # Assuming a method to encrypt password in Cipher class
            if success:
                flash('Your password has been updated!', 'success')
                return redirect(url_for('core.login'))  # Redirect to a home page or dashboard
            else:
                flash('There was an error updating your password.', 'danger')
        else:
            flash('Old password is incorrect.', 'danger')
    return render_template('update_password.html', form=form)