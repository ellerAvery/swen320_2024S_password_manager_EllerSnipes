from flask import Blueprint, flash, jsonify, redirect, render_template, request, session, url_for
from flask_login import current_user, login_required
from crypto.Cipher import Cipher
from web.user_management import decrypt_password, encrypt_password, get_user_token

core_bp = Blueprint("core", __name__)

@core_bp.route("/encrypt", methods=["GET", "POST"])
@login_required
def encrypt():
    encrypted_text = None
    if request.method == "POST":
        password_text = request.form.get('passwordTextE')
        user_token = get_user_token(current_user.username)  # Get user token using a defined function
        
        cipher = Cipher()  # Instantiate Cipher class (adjust if it requires a token)
        encrypted_text = cipher.encrypt(password_text, user_token)  # Encrypt using the user's token
        
        if 'encrypted_passwords' not in session:
            session['encrypted_passwords'] = []
        session['encrypted_passwords'].append({'password': encrypted_text, 'key': user_token})
        session.modified = True
        
        flash("Encryption successful!", "success")
    return render_template("core/encrypt.html", encrypted_text=encrypted_text)

@core_bp.route("/decrypt", methods=["GET", "POST"])
@login_required
def decrypt():
    decrypted_text = None
    if request.method == "POST":
        encrypted_text = request.form.get('encryptedTextD')
        user_token = get_user_token(current_user.username)  # Get user token
        
        cipher = Cipher()  # Instantiate Cipher class (adjust if it requires a token)
        decrypted_text = cipher.decrypt(encrypted_text, user_token)  # Decrypt the text
        
        if decrypted_text is None:
            flash("Decryption failed. Check your input and try again.", "danger")
        else:
            flash("Decryption successful!", "success")
    
    return render_template("core/decrypt.html", decrypted_text=decrypted_text)

@core_bp.route("/")
@login_required
def home():
    return redirect(url_for('.encrypt'))

@core_bp.route("/list")
@login_required
def list_encrypted():
    encrypted_passwords = session.get('encrypted_passwords', [])
    return render_template("core/list.html", encrypted_passwords=encrypted_passwords)

@core_bp.route('/Maketable')
def make_table():
    encrypted_list = session.get('encrypted_passwords', [])
    return jsonify(encrypted_list)

@core_bp.route('/saveEncryptedPassword', methods=['POST'])
def save_encrypted_password():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid or missing JSON data'}), 400
    
    # Implement the logic to save the encrypted data
    # For now, let's just simulate by adding to session
    if 'encrypted_passwords' not in session:
        session['encrypted_passwords'] = []
    session['encrypted_passwords'].append(data)
    session.modified = True
    
    return jsonify({'message': 'Encrypted password saved', 'receivedData': data}), 200
