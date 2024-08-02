from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Habit(db.Model):
    __tablename__ = 'habits'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    entries = db.relationship('HabitEntry', backref='habit', lazy=True)

class HabitEntry(db.Model):
    __tablename__ = 'habit_entries'
    id = db.Column(db.Integer, primary_key=True)
    habit_id = db.Column(db.Integer, db.ForeignKey('habits.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.Boolean, default=False, nullable=False)
