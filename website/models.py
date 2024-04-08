from flask_login import UserMixin, current_user
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, ForeignKey, Integer, String
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.mapped_column(db.Integer, primary_key=True)
    first_name = db.mapped_column(db.String(150), nullable=False)
    last_name = db.mapped_column(db.String(150), nullable=False)
    email = db.mapped_column(db.String(150), nullable=False, unique=True)
    password = db.mapped_column(db.String(150), nullable=False)

    def __str__(self):
        return self.first_name

class DiaryEntry(db.Model):
    __tablename__ = 'diary'
    id = db.mapped_column(db.Integer, primary_key=True)
    title = db.mapped_column(db.String(50), nullable=False)
    content = db.mapped_column(db.Text, nullable=False)
    created_at = db.mapped_column(db.DateTime, default=datetime.utcnow)
    user_id = db.mapped_column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('diary_entry', lazy=True))

    def __str__(self):
        return f'"{self.title}" by {self.user.first_name} ({self.created_at:%d-%m-%Y})'

class Tasks(db.Model):
    __tablename__ = 'tasks'
    id = db.mapped_column(db.Integer, primary_key=True)
    event_title = db.mapped_column(db.String(50), nullable=False)
    event_description = db.mapped_column(db.Text, nullable=False)
    start_time = db.mapped_column(db.DateTime, nullable=False)
    end_time = db.mapped_column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, default=lambda: current_user.id)
    user = db.relationship('User', backref=db.backref('tasks', lazy=True))

    def __str__(self):
        return f'"{self.event_title}":  {self.event_description} | {self.start_time:%d-%m-%Y} - {self.end_time}'