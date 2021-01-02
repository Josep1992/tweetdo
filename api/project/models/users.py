from project import db
from project.models.base import Base

class Users(Base):
    __tablename__ = "users"
    
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
