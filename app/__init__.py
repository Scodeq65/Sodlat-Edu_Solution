#!/usr/bin/env python3

"""
Initialize the Flask application and configure it.
"""

from flask import Flask
from flask_migrate import Migrate
from app.models import db
from flask_login import LoginManager
from app.routes.main import main
from app.routes.auth import auth


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize the database and migration
    db.init_app(app)
    migrate = Migrate(app, db)

    # Initialize Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    # Register Blueprints
    app.register_blueprint(main)

    return app
