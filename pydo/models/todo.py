from pydo import db
from pydo.models.base import Base

class Todo(Base):
    todo = db.Column(db.String,nullable=True)
    completed = db.Column(db.Boolean,default=False)

    def __repr__(self):
        return f"Todo('{self.todo}')('{self.completed}')"
