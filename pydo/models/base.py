from pydo import db
from datetime import datetime

class Base(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    # todos = db.relationship('Todo',backref='todos',lazy=True)

    def __repr__(self):
        return f"Base('{self.id}')('{self.date_created}')"
