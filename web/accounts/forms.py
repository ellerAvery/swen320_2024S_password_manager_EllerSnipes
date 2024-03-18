from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length

from web.accounts.models import User
class LoginForm(FlaskForm):
    username = StringField('User', validators=[DataRequired(), User()])
    password = PasswordField('Password', validators=[DataRequired()])

class RegisterForm(FlaskForm):
    username = StringField('User', validators=[DataRequired(), User()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=20)])
    token = StringField('Token', validators=[DataRequired(), Length(min=10, max=30)])
