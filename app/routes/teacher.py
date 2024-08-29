# Teacher dashboard

from flask import Blueprint, render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app.models import Course, Assignment, db

teacher = Blueprint('teacher', __name__)

@teacher.route('/teacher/dashboard')
@login_required
def teacher_dashboard():
    courses = Course.query.filter_by(teacher_id=current_user.id).all()
    return render_template('teacher_dashboard.html', courses=courses)

@teacher.route('/teacher/course/<int:course_id>/assignments', methods=['GET', 'POST'])
@login_required
def manage_assignments(course_id):
    course = Course.query.get_or_404(course_id)
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = request.form['due_date']
        assignment = Assignment(title=title, description=description, due_date=due_date, course_id=course.id)
        db.session.add(assignment)
        db.session.commit()
        return redirect(url_for('teacher.manage_assignments', course_id=course.id))
    assignments = Assignment.query.filter_by(course_id=course.id).all()
    return render_template('manage_assignments.html', course=course, assignments=assignments)