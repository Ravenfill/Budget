from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import defaultload
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/database.db'
db = SQLAlchemy(app)

class Expences(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255), nullable=False)
    product = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        item_category = request.form['category']
        item_product = request.form['product']
        item_price = request.form['price']
        new_item = Expences(category=item_category, product=item_product, price=item_price)

        try:
            db.session.add(new_item)
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue adding your task"

    else:
        items = Expences.query.order_by(Expences.id).all()
        return render_template(
            'index.html',
            categories=[{'name':'Продукты'}, {'name':'Развлечения'}],
            items=items, datetime = str(datetime.now().strftime("%A, %d %B %Y")))

@app.errorhandler(404)
def page_not_fount(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)