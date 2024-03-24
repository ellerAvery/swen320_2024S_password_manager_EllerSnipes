from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, ValidationError
from wtforms.validators import DataRequired


# Import necessary modules from flask_wtf and wtforms

# Define a form for user login
class LoginForm(FlaskForm):
    # Define fields for username and password, both are required fields
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])

# Define a form for user registration
class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    token = StringField("Passkey (Token)", validators=[DataRequired()])

    def validate(self, extra_validators=None):
        from web.user_management import get_users
        initial_validation = super(RegisterForm, self).validate(extra_validators=extra_validators)
        if not initial_validation:
            return False

        user = get_users(self.username.data)
        if user:
            self.username.errors.append("Username already registered")
            return False
        
        if len(self.username.data) < 5 or len(self.username.data) > 10:
            self.username.errors.append("Username must be between 5 and 10 characters long.")
            return False
        if len(self.password.data) < 8 or len(self.password.data) > 20:
            self.password.errors.append("Password must be between 8 and 20 characters long.")
            return False
        if len(self.token.data) < 10 or len(self.token.data) > 30:
            self.token.errors.append("Passkey must be between 10 and 30 characters long.")
            return False
        
        return True
# Define a form for changing password
class ChangePasswordForm(FlaskForm):
    old_password = PasswordField("Old Password", validators=[DataRequired()])
    new_password = PasswordField("New Password", validators=[DataRequired()])

    def validate_new_password(self, field):
        if len(field.data) < 8 or len(field.data) > 20:
            raise ValidationError("New password must be between 8 and 20 characters long.")

