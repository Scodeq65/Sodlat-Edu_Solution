#!/usr/bin/env python3

"""
Configuration settings for the Flask application.
"""

import os


class Config:
    """ Retrive d SECRET_KEY from d environment variable or use a default"""
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_secret_key')

    """ Retrive d database URI 4rm d environament variable or
    use a default SQLite database
    """
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///site.db')

    """ Retrieve the DEBUG mode setting from the environment
    variable or default to True
    """
    DEBUG = os.getenv('DEBUG', True)
