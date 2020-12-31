from pydo import db
from pydo.models.base import Base
from pydo.utils import generate_id
class Todo(Base):
    __tablename__ = "todos"
    id = db.Column(db.String, primary_key=True,default=generate_id)
    todo = db.Column(db.String,nullable=True)
    completed = db.Column(db.Boolean,default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"Todo('{self.todo}')('{self.completed}')"

    @property
    def to_object(self):
        return {
            'todo': self.todo,
            'completed': self.completed,
            'id': self.id,
            'date_created': self.date_created,
            'date_updated': self.date_updated,
            'user_id': self.user_id
        }
