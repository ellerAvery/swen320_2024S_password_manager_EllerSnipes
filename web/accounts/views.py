from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_user, current_user, login_required, logout_user
from web import db
from web.accounts.models import User
from .forms import LoginForm, RegisterForm

accounts_bp = Blueprint("accounts", __name__, url_prefix="/accounts")

@accounts_bp.route("/register", methods=["GET", "POST"])
def account_register():
    if current_user.is_authenticated:
        flash("You are already registered.", "info")
        return redirect(url_for("core.home"))
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first():
            flash("Email already registered.", "warning")
            return render_template("accounts/register.html", form=form)
        
        user = User(email=form.email.data)
        user.set_password(form.password.data)  # Ensure this method hashes the password
        user.token = form.token.data
        db.session.add(user)
        db.session.commit()

        login_user(user)
        flash("Welcome! Account created successfully.", "success")
        return redirect(url_for("core.home"))
    return render_template("accounts/register.html", form=form)

@accounts_bp.route("/login", methods=["GET", "POST"])
def account_login():
    if current_user.is_authenticated:
        flash("You are already logged in.", "info")
        return redirect(url_for("core.home"))
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for("core.home"))
        else:
            flash("Invalid email and/or password.", "error")
    return render_template("accounts/login.html", form=form)

@accounts_bp.route("/logout")
@login_required
def account_logout():
    logout_user()
    flash("You have been logged out.", "success")
    return redirect(url_for("accounts.account_login"))



