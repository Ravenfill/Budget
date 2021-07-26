from app import db
from datetime import datetime

class Expences(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255), nullable=False)
    product = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

# TODO: Add categories
#class Category():
#    id = db.Column(db.Integer, primary_key=True)
#    category = db.Column(db.String(255), nullable=False) 
#    image = db.Column(db.LargeBinary, nullable = True)