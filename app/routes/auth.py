#!/usr/bin/python3
"""
Authentication routes for registration and login.
"""

from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User, db, Child
from app.forms import RegistrationForm, LoginForm

auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            role=form.role.data
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        if form.role.data == 'parent':
            # Register children for the parent
            for child_name in form.children.data.split(','):
                first_name, last_name = child_name.strip().split(' ')
                child = Child(
                    first_name=first_name,
                    last_name=last_name,
                    parent_id=user.id
                )
                db.session.add(child)
            db.session.commit()

        flash('Registration successful. You can now log in.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html', form=form, welcome_message="Welcome! Please create an account.")


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect_user_based_on_role()

    form = LoginForm()
    if form.validate_on_submit():
        identifier = form.identifier.data
        user = User.query.filter((User.username == identifier) | (User.email == identifier)).first()

        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash('Login successful.', 'success')
            return redirect_user_based_on_role()
        else:
            flash('Invalid login credentials. Please try again.', 'danger')

    return render_template('login.html', form=form, welcome_message="Welcome back!")


def redirect_user_based_on_role():
    if current_user.role == 'parent':
        return redirect(url_for('main.parent_dashboard'))
    elif current_user.role == 'teacher':
        return redirect(url_for('main.teacher_dashboard'))
    elif current_user.role == 'student':
        return redirect(url_for('main.student_dashboard'))
    else:
        logout_user()
        flash('Invalid role detected. Please log in again.', 'danger')
        return redirect(url_for('auth.login'))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('main.index'))