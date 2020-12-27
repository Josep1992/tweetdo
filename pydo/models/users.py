from pydo import db
from pydo.models.base import Base

class Users(Base):
    email = db.Column(db.String(100), nullable=False,unique=True)
    password = db.Column(db.String(60), nullable=False)
    # todos = db.relationship('Todo',backref='todos',lazy=True)

    def __repr__(self):
        return f"User('{self.email}')('{self.password}')"

    @property
    def to_object(self):
        return {
            'email': self.email,
            'password': self.password,
            'id': self.id,
            'date_created': self.date_created,
            'date_updated': self.date_updated
        }
