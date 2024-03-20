from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import logout_user, login_required, current_user, login_user
from web.accounts.models import User
from .forms import LoginForm, RegisterForm, ChangePasswordForm
from web.user_management import add_users, get_users, check_password, encrypt_password, decrypt_password

# Create a Blueprint for accounts
accounts_bp = Blueprint('accounts', __name__)

# Route for user registration
@accounts_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # Attempt to add user to the database
        success = add_users(form.username.data, form.password.data, form.token.data)
        if success:
            flash('Registration successful!', 'success')
            return redirect(url_for('accounts.login'))
        else:
            flash('User already exists.', 'danger')
    return render_template('accounts/register.html', form=form)

# Route for user login
@accounts_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Check if user exists and password is correct
        user_info = get_users(form.username.data)
        if user_info and check_password(form.username.data, form.password.data):
    # Pass the username to the User constructor
            user = User(username=form.username.data)
            user.id = form.username.data  # This line might be redundant if the id is set within the User constructor
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('core.encrypt'))
        else:
            flash('Invalid username or password.', 'danger')
    return render_template('accounts/login.html', form=form)

# Route for user logout
@accounts_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('accounts.login'))

# Route for updating password
@accounts_bp.route('/update_password', methods=['GET', 'POST'])
@login_required
def update_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        # Check if old password is correct
        user_info = get_users(current_user.username)
        if user_info and check_password(current_user.username, form.old_password.data):
            # Attempt to update password
            success = update_password(current_user.username, encrypt_password(form.new_password.data))
            if success:
                flash('Your password has been updated!', 'success')
                return redirect(url_for('accounts.login'))
            else:
                flash('There was an error updating your password.', 'danger')
        else:
            flash('Old password is incorrect.', 'danger')
    return render_template('accounts/updatepass.html', form=form)
