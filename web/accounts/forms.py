from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField
from wtforms.validators import DataRequired, Email, Length
from web.accounts.models import User


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])

    def loginExists(email, password):
        loginUser = User()

        loginUser.email = email
        loginUser.password = password

        for(User in users):
            if(loginUser.email == User.email and loginUser.password == User.password):
                return True
        
        return False



class RegisterForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email(message=None), Length(min=5, max=10)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=20)])
    token = StringField("Passkey (Token)", validators=[DataRequired(), Length(min=10, max=30)])


    def validate(self, extra_validators=None):
        initial_validation = super(RegisterForm, self).validate(extra_validators=extra_validators)
        if not initial_validation:
            return False
        user = User.query.filter_by(email=self.email.data).first()
        if user:
            self.email.errors.append("Email already registered")
            return False
        return True
    
    def passLenValid(self):
        if(self.password.Length < 20 and self.password.Length > 8):
            return True
        else:
            self.email.errors.append("Invalid password length")
            return False

    def userLenValid(self):
        if(self.email.Length < 10 and self..Length > 5):
            return True
        else:
            self.email.errors.append("Invalid email length")
            return False

    def keyLenValid(self):
        if(self.passkey.Length < 30 and self.passkey.Length > 10):
            return True
        else:
            self.email.errors.append("Invalid self.passkey length")
            return False
