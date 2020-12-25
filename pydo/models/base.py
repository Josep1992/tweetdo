from pydo import db
from datetime import datetime

class Base(db.Model):
    id = db.Column(db.Integer, primary_key=True,auto_increment=True)
    date_created = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    date_updated = db.Column(db.DateTime,nullable=False,default=datetime.utcnow())

    def __repr__(self):
        return f"Base('{self.id}')('{self.date_created}')"
