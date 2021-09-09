from app import db
from datetime import datetime, timedelta
from flask_login import current_user

## Expences table
class Expences(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255), nullable=False)
    product = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float)
    user = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

class MonthExpencesProfile():
    first_exps = 0
    first_date = datetime.utcnow()
    second_exps = 0
    second_date = first_date.replace(day=1) - timedelta(days=1)
    third_exps = 0
    third_date = second_date.replace(day=1) - timedelta(days=1)
    fourth_exps = 0
    fourth_date = third_date.replace(day=1) - timedelta(days=1)
    fifth_exps = 0
    fifth_date = fourth_date.replace(day=1) - timedelta(days=1)

    def __init__(self):
        exps = Expences.query.filter_by(user=current_user.id).order_by(Expences.date_created.desc()).all()
        for exp in exps:
            if exp.date_created.utcnow().strftime("%Y-%m") == self.first_date.strftime("%Y-%m"):
                self.first_exps += exp.price
            elif exp.date_created.utcnow().strftime("%Y-%m") == self.second_date.strftime("%Y-%m"):
                self.second_exps += exp.price
            elif exp.date_created.utcnow().strftime("%Y-%m") == self.third_date.strftime("%Y-%m"):
                self.third_exps += exp.price
            elif exp.date_created.utcnow().strftime("%Y-%m") == self.fourth_exps.strftime("%Y-%m"):
                self.fourth_exps += exp.price
            elif exp.date_created.utcnow().strftime("%Y-%m") == self.fifth_date.strftime("%Y-%m"):
                self.fifth_exps += exp.price
        
        exp_n = [self.first_exps, self.second_exps, self.third_exps, self.fourth_exps, self.fifth_exps]
        exp_d = [self.first_date.strftime("%B"), self.second_date.strftime("%B"), self.third_date.strftime("%B"), self.fourth_date.strftime("%B"), self.fifth_date.strftime("%B")]

        self._data = []
        for i in range(0, 5):
            if exp_n[i] != 0:
                self._data.append((exp_d[i], exp_n[i]))

    def __getitem__(self, position):
        return self._data[position]