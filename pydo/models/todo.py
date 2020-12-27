from pydo import db
from flask import jsonify
from pydo.models.base import Base

class Todo(Base):
    todo = db.Column(db.String,nullable=True)
    completed = db.Column(db.Boolean,default=False)

    def __repr__(self):
        return f"Todo('{self.todo}')('{self.completed}')"

    @property
    def to_object(self):
        return {
            'todo': self.todo,
            'completed': self.completed,
            'id': self.id,
            'date_created': self.date_created,
            'date_updated': self.date_updated
        }