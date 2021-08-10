from app import db
from datetime import datetime

class Expences(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255), nullable=False)
    product = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float)
    user = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

class MonthlyExps(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer)
    monthly_expences = db.Column(db.Float, nullable=True)
    previous_month_exps = db.Column(db.Float, nullable=True)
    date_updated = db.Column(db.DateTime, default=datetime.utcnow)