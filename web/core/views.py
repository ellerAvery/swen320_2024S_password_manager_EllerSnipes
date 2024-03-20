from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from flask_login import login_required
from crypto.Cipher import Cipher
from web.user_management import encrypt_password, decrypt_password
# Create a Blueprint object for the core part of the application
core_bp = Blueprint("core", __name__)

# Define a route for encrypting passwords
@core_bp.route("/encrypt", methods=["GET", "POST"])
@login_required
def encrypt():
    encrypted_text = None
    if request.method == "POST":
        password_text = request.form.get('passwordTextE')
        key_text = request.form.get('key', None)  # Use None as default to fall back to the default passkey
        cipher = Cipher()  # Instantiate your Cipher class
        try:
            encrypted_text = cipher.encrypt(password_text, passkey=key_text)  # Encrypt using the Cipher class
            flash("Encryption successful!", "success")
        except Exception as e:
            flash(f"Encryption failed: {str(e)}", "danger")
    return render_template("core/encrypt.html", encrypted_text=encrypted_text)

# Define a route for decrypting passwords
@core_bp.route("/decrypt", methods=["GET", "POST"])
@login_required  # Require the user to be logged in
def decrypt():
    decrypted_text = None  # Initialize as None to handle form state before submission
    if request.method == "POST":  # If the form is submitted
        encrypted_text = request.form.get('encryptedTextD')  # Get the encrypted password from the form
        try:
            decrypted_text = decrypt_password(encrypted_text)  # Try to decrypt the password
            if decrypted_text is None:  # If decryption fails
                flash("Decryption failed. Check your input and try again.", "danger")  # Show an error message
            else:
                flash("Decryption successful!", "success")  # If successful, show a success message
        except Exception as e:
            flash(f"Decryption failed: {str(e)}", "danger")  # If an error occurs, show an error message
    return render_template("core/decrypt.html", decrypted_text=decrypted_text)  # Render the decrypt page

# Define a default route that redirects to the encrypt page
@core_bp.route("/")
@login_required  # Require the user to be logged in
def home():
    return redirect(url_for('.encrypt'))  # Redirect to the encrypt page

# Define a route for listing encrypted passwords
@core_bp.route("/list")
@login_required  # Require the user to be logged in
def list():
    encrypted_list = session.get('encrypted_list', [])  # Get the list of encrypted passwords from the session
    return render_template("core/list.html", encrypted_list=encrypted_list)  # Render the list page
