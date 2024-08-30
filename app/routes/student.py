#!/usr/bin/python3
"""
Student routes for viewing assignments and submitting them.
"""

from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app.models import Assignment, db

student = Blueprint('student', __name__)


@student.route('/student/dashboard')
@login_required
def student_dashboard():
    courses = Course.query.all()
    assignments = Assignment.query.all()
    return render_template('student_dashboard.html', courses=courses, assignments=assignments)


"""@student.route('/student/assignment/<int:assignment_id>', methods=['GET', 'POST'])
@login_required
def submit_assignment(assignment_id):
    assignment = Assignment.query.get_or_404(assignment_id)
    if request.method == 'POST':
        # Assuming file upload or text submission is handled here.
        assignment.status = 'Submitted'
        db.session.commit()
        return redirect(url_for('student.student_dashboard'))

    return render_template('submit_assignment.html', assignment=assignment)


@student.route('/view_course_materials/<int:course_id>')
@login_required
def view_course_materials(course_id):
    if current_user.role != 'Student':
        return redirect(url_for('main.index'))

    course = Course.query.get_or_404(course_id)
    materials = course.materials  # Assuming you have a relationship or attribute for materials
    return render_template('view_course_materials.html', course=course, materials=materials)
"""