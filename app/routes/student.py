# Student dashmoard

from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models import Assignment

student = Blueprint('student', __name__)

@student.route('/student/dashboard')
@login_required
def student_dashboard():
    assignments = Assignment.query.filter_by(student_id=current_user.id).all()
    return render_template('student_dashboard.html', assignments=assignments)

@student.route('/student/assignment/<int:assignment_id>', methods=['GET', 'POST'])
@login_required
def submit_assignment(assignment_id):
    assignment = Assignment.query.get_or_404(assignment_id)
    if request.method == 'POST':
        # Handle file upload or text submission
        assignment.status = 'Submitted'
        db.session.commit()
        return redirect(url_for('student.student_dashboard'))
    return render_template('submit_assignment.html', assignment=assignment)