#!/usr/bin/python3
"""
Routes for the teacher dashboard.
"""

from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from app.models import Course, Assignment, User, db
from app.forms import CreateStudentForm, GradeAssignmentForm

teacher = Blueprint('teacher', __name__)

@teacher.route('/teacher/dashboard')
@login_required
def teacher_dashboard():
    courses = Course.query.filter_by(teacher_id=current_user.id).all()
    return render_template('teacher_dashboard.html', courses=courses)

@teacher.route('/teacher/course/<int:course_id>/assignments', methods=['GET', 'POST'])
@login_required
def course_assignments(course_id):
    """
    View and manage assignments for a specific course.
    """
    course = Course.query.get_or_404(course_id)
    if course.teacher_id != current_user.id:
        flash('Access denied.', 'danger')
        return redirect(url_for('teacher.teacher_dashboard'))

    assignments = Assignment.query.filter_by(course_id=course_id).all()

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = request.form['due_date']
        assignment = Assignment(
            title=title,
            description=description,
            due_date=due_date,
            course_id=course_id
        )
        db.session.add(assignment)
        db.session.commit()
        flash('Assignment created successfully.', 'success')
        return redirect(url_for('teacher.course_assignments', course_id=course_id))

    return render_template('course_assignments.html', course=course, assignments=assignments)

@teacher.route('/teacher/assignments/<int:assignment_id>/grade', methods=['GET', 'POST'])
@login_required
def grade_assignment(assignment_id):
    assignment = Assignment.query.get_or_404(assignment_id)
    form = GradeAssignmentForm()
    if form.validate_on_submit():
        assignment.status = form.status.data
        db.session.commit()
        flash('Assignment graded successfully.', 'success')
        return redirect(url_for('teacher.teacher_dashboard'))
    return render_template('grade_assignment.html', form=form, assignment=assignment)

@teacher.route('/teacher/students', methods=['GET', 'POST'])
@login_required
def manage_students():
    form = CreateStudentForm()
    if form.validate_on_submit():
        student = User(
            username=form.username.data,
            email=form.email.data,
            role='student'
        )
        student.set_password(form.password.data)
        db.session.add(student)
        db.session.commit()
        flash('Student account created successfully.', 'success')
        return redirect(url_for('teacher.manage_students'))

    students = User.query.filter_by(role='student').all()
    return render_template('manage_students.html', students=students, form=form)

@teacher.route('/teacher/students/<int:student_id>/assign-parent', methods=['POST'])
@login_required
def assign_parent(student_id):
    student = User.query.get_or_404(student_id)
    parent_id = request.form['parent_id']
    parent = User.query.get(parent_id)
    if not parent or parent.role != 'parent':
        flash('Invalid parent selection.', 'danger')
    else:
        student.parent_id = parent.id
        db.session.commit()
        flash(f'Parent {parent.username} assigned to student {student.username}.', 'success')
    return redirect(url_for('teacher.manage_students'))