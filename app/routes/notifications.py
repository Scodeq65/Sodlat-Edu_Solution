# notifications.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models import Notification

notifications = Blueprint('notifications', __name__)

@notifications.route('/notifications')
@login_required
def view_notifications():
    notifications = Notification.query.filter_by(user_id=current_user.id).order_by(Notification.timestamp.desc()).all()
    return render_template('notifications.html', notifications=notifications)