#!/usr/bin/env python3
"""
Forms for authentication and teacher management in the application.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    role = SelectField('Role', choices=[('parent', 'Parent'), ('student', 'Student'), ('teacher', 'Teacher')], validators=[DataRequired()])
    children = TextAreaField('Children Names (for Parents only)', description="Enter children names separated by commas (e.g., John Doe, Jane Doe)")
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    identifier = StringField('Username or Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')

class CreateStudentForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Create Student Account')

class GradeAssignmentForm(FlaskForm):
    status = SelectField('Status', choices=[('Completed', 'Completed'), ('Pending', 'Pending')], validators=[DataRequired()])
    submit = SubmitField('Submit Grade')