#!/usr/bin/env python3
"""This module defines the database models for SodLat Edu Solution."""

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class User(db.Model, UserMixin):
    """User model representing parents, teachers, and students."""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(50), nullable=False)

    # Relationships
    courses = db.relationship('Course', backref='teacher', lazy=True)
    assignments = db.relationship('Assignment', backref='student', lazy=True)

    def __repr__(self):
        return f"<User {self.username} - Role: {self.role}>"

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Course(db.Model):
    """Course model representing the courses managed by teachers."""
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    teacher_id = db.Column(
        db.Integer, db.ForeignKey('users.id'), nullable=False
    )

    # Relationships
    assignments = db.relationship('Assignment', backref='course', lazy=True)

    def __repr__(self):
        return f"<Course {self.name} - Teacher ID: {self.teacher_id}>"


class Assignment(db.Model):
    """Assignment model representing tasks assigned to students."""
    __tablename__ = 'assignments'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    due_date = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow
    )
    student_id = db.Column(
        db.Integer, db.ForeignKey('users.id'), nullable=False
    )
    course_id = db.Column(
        db.Integer, db.ForeignKey('courses.id'), nullable=False
    )

    def __repr__(self):
        return (
            f"<Assignment {self.title} - Student ID: {self.student_id} - "
            f"Course ID: {self.course_id}>"
        )
