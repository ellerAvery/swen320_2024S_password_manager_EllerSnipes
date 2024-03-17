from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=5, max=10)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    token = StringField('Passkey (Token)', validators=[DataRequired(), Length(min=10, max=30)])

