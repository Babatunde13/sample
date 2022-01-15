from typing import Dict
import uuid
from app import db

class UUID(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    uuid = db.Column(db.String(36), nullable=False, default=uuid.uuid4().hex)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())

    def __repr__(self):
        return '<UUID %r>' % self.uuid
    
    def save(self):
        db.session.commit()


def new_uuid() -> Dict[str, str]:
    '''
        Helper function to create a new UUID and return all existing UUIDs
    '''
    uuid_data = UUID()
    db.session.add(uuid_data)
    uuid_data.save()
    resp = {}
    for data in UUID.query.all():
        date = data.created_at.strftime("%Y-%m-%d %H:%M:%S:%f")
        resp[date] = data.uuid
    return resp
