from app import db
from datetime import datetime

class Expences(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255), nullable=False)
    product = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float)
    user = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)