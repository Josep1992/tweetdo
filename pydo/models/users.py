from pydo import db
from pydo.models.base import Base

class Users(Base):
    # id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False,unique=True)
    password = db.Column(db.String(60), nullable=False)
    # date_created = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    # todos = db.relationship('Todo',backref='todos',lazy=True)

    def __repr__(self):
        return f"User('{self.email}')('{self.password}')"
