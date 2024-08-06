from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CategoryHabit(db.Model):
    __tablename__ = 'categories_habits'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, index=True)
    description = db.Column(db.Text, nullable=True)
    habits = db.relationship('Habit', secondary='habits_categories', backref=db.backref('categories', lazy='dynamic'))

class HabitEntry(db.Model):
    __tablename__ = 'habit_entries'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, index=True)
    status = db.Column(db.Boolean, default=False, nullable=False, index=True)
    habits = db.relationship('Habit', secondary='habits_entries', backref=db.backref('entries', lazy='dynamic'))

class Habit(db.Model):
    __tablename__ = 'habits'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False, index=True)
    description = db.Column(db.Text, nullable=True)

class HabitCategories(db.Model):
    __tablename__ = 'habits_categories'
    id_habit = db.Column(db.Integer, db.ForeignKey('habits.id'), primary_key=True)
    id_category = db.Column(db.Integer, db.ForeignKey('categories_habits.id'), primary_key=True)
    db.Index('idx_habit_category', 'id_habit', 'id_category')

class HabitEntries(db.Model):
    __tablename__ = 'habits_entries'
    id_habit = db.Column(db.Integer, db.ForeignKey('habits.id'), primary_key=True)
    id_entry = db.Column(db.Integer, db.ForeignKey('habit_entries.id'), primary_key=True)
    db.Index('idx_habit_entry', 'id_habit', 'id_entry')
