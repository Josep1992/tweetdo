from pydo import db
from datetime import datetime
from uuid import uuid4

def generate_id():
    return str(uuid4())

class Base(db.Model):
    id = db.Column(db.String, primary_key=True,default=generate_id)
    date_created = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    date_updated = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)

    def __repr__(self):
        return f"Base('{self.id}')('{self.date_created}')"
