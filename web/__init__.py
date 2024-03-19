from flask import Flask, request, redirect, url_for, render_template, flash
from crypto.Cipher import Cipher
import pickle

app = Flask(__name__)
users = {}

def load_users():
    global users
    try:
        with open('users.pickle', 'rb') as f:
            users = pickle.load(f)
    except FileNotFoundError:
        pass

def save_users():
    with open('users.pickle', 'wb') as f:
        pickle.dump(users, f)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users:
            flash('Username already taken. Please choose another one.')
            return redirect(url_for('register'))
        
        cipher = Cipher()
        encrypted_password = cipher.encrypt(password)
        users[username] = encrypted_password
        save_users()
        flash('Registration successful!')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.before_first_request
def before_first_request():
    load_users()

@app.teardown_appcontext
def teardown_appcontext(exception=None):
    save_users()

if __name__ == '__main__':
    app.run(debug=True)
