from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from flask_login import login_required
from web.user_management import encrypt_password, decrypt_password


core_bp = Blueprint("core", __name__)

@core_bp.route("/encrypt", methods=["GET", "POST"])
@login_required
def encrypt():
    encrypted_text = None  # Initialize as None to handle form state before submission
    if request.method == "POST":
        password_text = request.form.get('passwordTextE')
        key_text = request.form.get('key', 'default_key')  # Use a default or provided key
        try:
            encrypted_text = encrypt_password(password_text, key_text)
            flash("Encryption successful!", "success")
        except Exception as e:
            flash(f"Encryption failed: {str(e)}", "danger")
    return render_template("core/encrypt.html", encrypted_text=encrypted_text)

@core_bp.route("/decrypt", methods=["GET", "POST"])
@login_required
def decrypt():
    decrypted_text = None  # Initialize as None to handle form state before submission
    if request.method == "POST":
        encrypted_text = request.form.get('encryptedTextD')
        try:
            decrypted_text = decrypt_password(encrypted_text)
            if decrypted_text is None:
                flash("Decryption failed. Check your input and try again.", "danger")
            else:
                flash("Decryption successful!", "success")
        except Exception as e:
            flash(f"Decryption failed: {str(e)}", "danger")
    return render_template("core/decrypt.html", decrypted_text=decrypted_text)


@core_bp.route("/")
@login_required
def home():
    # Directing to the encrypt page as a default action for simplicity
    return redirect(url_for('.encrypt'))

@core_bp.route("/list")
@login_required
def list():
    encrypted_list = session.get('encrypted_list', [])
    return render_template("core/list.html", encrypted_list=encrypted_list)
