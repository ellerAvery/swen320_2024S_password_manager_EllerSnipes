from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required
from web.user_management import encrypt_password, decrypt_password


core_bp = Blueprint("core", __name__)

@core_bp.route("/encrypt", methods=["GET", "POST"])
@login_required
def encrypt():
    if request.method == "POST":
        password_text = request.form.get('passwordTextE')
        key_text = request.form.get('key')
        # Assume the key_text is the passkey/token for additional security, or a separate key if implemented
        encrypted_text = encrypt_password(password_text, key_text)
        return render_template("core/encrypt.html", encrypted_text=encrypted_text)
    return render_template("core/encrypt.html")

@core_bp.route("/decrypt", methods=["GET", "POST"])
@login_required
def decrypt():
    if request.method == "POST":
        encrypted_text = request.form.get('encryptedTextD')
        decrypted_text = decrypt_password(encrypted_text)
        return render_template("core/decrypt.html", decrypted_text=decrypted_text)
    return render_template("core/decrypt.html")

@core_bp.route("/")
@login_required
def home():
    # Directing to the encrypt page as a default action for simplicity
    return redirect(url_for('.encrypt'))

@core_bp.route("/list")
@login_required
def list():
    # This would list all encrypted passwords and their tags for the current user
    # Since we're not using a database, this functionality might need a custom implementation
    # For demonstration purposes, redirect to home or another placeholder page
    flash("This feature requires implementation.", "info")
    return redirect(url_for('.home'))
