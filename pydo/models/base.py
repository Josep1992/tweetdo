from pydo import db
from datetime import datetime

class Base(db.Model):
    __abstract__ = True

    date_created = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    date_updated = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    index = db.Column(db.Integer,auto_increment=True)

    def __repr__(self):
        return f"Base('{self.id}')('{self.date_created}')"
