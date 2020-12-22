from pydo import db
from pydo.models.base import Base

class User(Base):
    email = db.Column(db.String(100), nullable=False,unique=True)
    password = db.Column(db.String(60), nullable=False)
    # todos = db.relationship('Todo',backref='todos',lazy=True)

    def __repr__(self):
        return f"User('{self.email}')('{self.password}')"
