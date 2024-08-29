#!/usr/bin/env python3

"""
Defines the main routes for the application
and initializes the database.
"""

from flask import Blueprint, render_template, redirect, url_for, flash, abort
from flask_login import login_required, current_user
from functools import wraps


main = Blueprint('main', __name__)


def role_required(role):
    """
    Decorator to check if the user has the required role.
    """
    def wrapper(fn):
        @wraps(fn)
        @login_required
        def decorated_view(*args, **kwargs):
            if current_user.role != role:
                flash('Access denied.', 'danger')
                return redirect(url_for('main.index'))
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper


def forbidden_if_not_allowed(fn):
    """
    Decorator to check if the user has permission to access the page.
    """
    @wraps(fn)
    def decorated_view(*args, **kwargs):
        if not current_user.is_authenticated:
            abort(403)  
        return fn(*args, **kwargs)
    return decorated_view


@main.route('/')
@login_required
def index():
    """
    Render the homepage.
    """
    return render_template('index.html')


@main.route('/parent')
@role_required('parent')
def parent_dashboard():
    """
    Render the parent dashboard.
    """
    return render_template('parent_dashboard.html')


@main.route('/teacher')
@role_required('teacher')
def teacher_dashboard():
    """
    Render the teacher dashboard.
    """
    return render_template('teacher_dashboard.html')


@main.route('/student')
@role_required('student')
def student_dashboard():
    """
    Render the student dashboard.
    """
    return render_template('student_dashboard.html')


@main.errorhandler(403)
def forbidden_error(error):
    """
    Handle 403 errors.
    """
    return render_template('403.html'), 403