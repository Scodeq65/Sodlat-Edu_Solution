# parent dashboard

from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models import ChildProgress, Assignment

parent = Blueprint('parent', __name__)

@parent.route('/parent/dashboard')
@login_required
def parent_dashboard():
    # Assuming the parent can view multiple children's progress
    children_progress = ChildProgress.query.filter_by(child_id=current_user.id).all()
    assignments = Assignment.query.filter_by(student_id=current_user.id).all()
    return render_template('parent_dashboard.html', children_progress=children_progress, assignments=assignments)