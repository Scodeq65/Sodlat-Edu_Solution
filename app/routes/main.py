#!/usr/bin/env python3

"""
Defines the main routes for the application
and initializes the database.
"""

from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db


main = Blueprint('main', __name__)


@main.route('/')
def index():
    """
    Render the homepage.
    """
    return render_template('index.html')

@main.route('/parent')
@login_required
def parent_dashboard():
    """
    Render the parent dashboard.
    """
    if current_user.role != 'parent':
        flash('Access denied.', 'danger')
        return redirect(url_for('main.index'))
    return render_template('parent_dashboard.html')

@main.route('/teacher')
@login_required
def teacher_dashboard():
    """
    Render the teacher dashboard.
    """
    if current_user.role != 'teacher':
        flash('Access denied.', 'danger')
        return redirect(url_for('main.index'))
    return render_template('teacher_dashboard.html')

@main.route('/student')
@login_required
def student_dashboard():
    """
    Render the student dashboard.
    """
    if current_user.role != 'student':
        flash('Access denied.', 'danger')
        return redirect(url_for('main.index'))
    return render_template('student_dashboard.html')
