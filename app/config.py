#!/usr/bin/env python3

"""
Configuration settings for the Flask application.
"""

import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    """ Retrive d SECRET_KEY from d environment variable or use a default"""
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_secret_key')

    """ Retrive d database URI 4rm d environament variable or
    use a default SQLite database
    """
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///sodlat_edu_solution.db')

    """Retrieve the DEBUG mode setting from the environment
    variable or default to False.
    """
    DEBUG = os.getenv('DEBUG', False).lower() in ['true', '1']


    """Enable/disable tracking modifications of objects and
    emit signals. Default is False.
    """
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    """Configure session cookie settings."""
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = os.getenv('SESSION_COOKIE_SECURE', False).lower() in ['true', '1']
    REMEMBER_COOKIE_DURATION = int(os.getenv('REMEMBER_COOKIE_DURATION', 604800))
