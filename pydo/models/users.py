from pydo import db
from pydo.models.base import Base
from pydo.utils import generate_id
class Users(Base):
    __tablename__ = "users"
    id = db.Column(db.String, primary_key=True,default=generate_id)
    email = db.Column(db.String(100), nullable=False,unique=True)
    password = db.Column(db.String(60), nullable=False)
    todos = db.relationship('Todo',backref='todos',lazy=True)
    # @on relationship Todo -- refers to the Todo MODEL and the backref refers to the @__tablename 

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
