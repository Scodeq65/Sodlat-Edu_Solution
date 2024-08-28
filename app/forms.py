from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, BooleanField,
    SubmitField, SelectField
)
from wtforms.validators import DataRequired, Email, EqualTo


class RegistrationForm(FlaskForm):
    """Form for user registration."""
    username = StringField('Username or Email', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')]
    )
    role = SelectField(
        'Role',
        choices=[
            ('parent', 'Parent'),
            ('teacher', 'Teacher'),
            ('student', 'Student')
        ],
        validators=[DataRequired()]
    )
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    """Form for user login."""
    identifier = StringField('Username or Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
