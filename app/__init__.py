#!/usr/bin/env python3

"""
Initialize the Flask application and configure it.
"""

from flask import Flask
from flask_migrate import Migrate
from app.models import db
from app.routes.main import main


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize the database and migration
    db.init_app(app)
    migrate = Migrate(app, db)

    # Register Blueprints
    app.register_blueprint(main)

    return app
