from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired, Length


# Import necessary modules from flask_wtf and wtforms

# Define a form for user login
class LoginForm(FlaskForm):
    # Define fields for username and password, both are required fields
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])

# Define a form for user registration
class RegisterForm(FlaskForm):
    # Define fields for username, password, and token. All are required fields.
    # Username must be between 5 and 10 characters, password between 8 and 20, and token between 10 and 30.
    username = StringField("Username", validators=[DataRequired(), Length(min=5, max=10)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=20)])
    token = StringField("Passkey (Token)", validators=[DataRequired(), Length(min=10, max=30)])

    # Define a custom validation method for the form
    def validate(self, extra_validators=None):
        from web.user_management import get_users 
        # Perform initial validation
        initial_validation = super(RegisterForm, self).validate(extra_validators=extra_validators)
        # If initial validation fails, return False
        if not initial_validation:
            return False
        # Check if the username is already registered
        user = get_users(self.username.data)  # Using custom user management function
        # If the username is already registered, append an error message and return False
        if user:
            self.username.errors.append("Username already registered")
            return False
        # If all checks pass, return True
        return True

# Define a form for changing password
class ChangePasswordForm(FlaskForm):
    # Define fields for old password and new password, both are required fields
    # New password must be between 8 and 20 characters
    old_password = PasswordField("Old Password", validators=[DataRequired()])
    new_password = PasswordField("New Password", validators=[DataRequired(), Length(min=8, max=20)])
