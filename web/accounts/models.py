# Where the accounts are being stored in.
from flask_login import UserMixin
from web import db
from crypto.Cipher import Cipher

class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    token = db.Column(db.String, nullable=False)

    def __init__(self, email, password, token):
        self.email = email
        cipher = Cipher()
        encText = cipher.encrypt(password)
        self.password = encText
        self.token = token


    def __repr__(self):
        return f"<email {self.email}>"
    
    def check_password(self, password):
        cipher = Cipher();
        return cipher.decrypt(self.password) == password