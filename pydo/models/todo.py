from pydo import db
from pydo.models.base import Base

class Todo(Base):
    __tablename__ = "todos"
    
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
