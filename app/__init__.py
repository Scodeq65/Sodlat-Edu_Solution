#!/usr/bin/env python3

"""
Initialize the Flask application and configure it.
"""

from flask import Flask
from app.routes.main import main


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Register Blueprints
    app.register_blueprint(main)

    return app
