#!/usr/bin/env python3

"""
Defines the main routes for the application.
"""

from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    """
    Render the homepage.
    """
    return render_template('index.html')

@main.route('/parent')
def parent_dashboard():
    """
    Render the parent dashboard.
    """
    return render_template('parent_dashboard.html')

@main.route('/teacher')
def teacher_dashboard():
    """
    Render the teacher dashboard.
    """
    return render_template('teacher_dashboard.html')

@main.route('/student')
def student_dashboard():
    """
    Render the student dashboard.
    """
    return render_template('student_dashboard.html')