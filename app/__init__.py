#!/usr/bin/env python3
"""
Initialize the SodLat Edu Solution application.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)

    from app.routes.main import main
    from app.routes.auth import auth
    from app.routes.teacher import teacher
    from app.routes.student import student
    from app.routes.parent import parent

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(teacher)
    app.register_blueprint(student)
    app.register_blueprint(parent)

    return app