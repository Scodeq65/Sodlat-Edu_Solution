#!/usr/bin/env python3
"""
Routes for the parent dashboard.
"""

from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models import Child, ChildProgress


parent = Blueprint('parent', __name__)


@parent.route('/parent/dashboard')
@login_required
def parent_dashboard():
    children = Child.query.filter_by(parent_id=current_user.id).all()
    progress = {child.id: ChildProgress.query.filter_by(child_id=child.id).all() for child in children}
    return render_template('parent_dashboard.html', children=children, progress=progress)