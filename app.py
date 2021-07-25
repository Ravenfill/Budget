from flask import Flask, render_template, request, redirect
from flask_wtf import Form
from wtforms import StringField, FloatField, SelectField, SubmitField, DecimalField
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import defaultload
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/database.db'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'dwodkwadwad'


# TODO: Add categories
class Category():
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255), nullable=False) 
    image = db.Column(db.LargeBinary, nullable = True)

class AddExpenceForm(Form):
    category_select = SelectField(choices=['Продукты', 'Развлечения'])
    product_name = StringField('Продукт')
    price_value = DecimalField('Цена')
    submit = SubmitField('submit')

class Expences(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255), nullable=False)
    product = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/', methods=['POST', 'GET'])
def index():
    monthly_expences = 0
    form = AddExpenceForm()
    # Adding new items
    if request.method == 'POST' and form.validate():
        item_category = form.category_select.data
        item_product = form.product_name.data
        item_price = form.price_value.data
        new_item = Expences(category=item_category, product=item_product, price=item_price)
        db.session.add(new_item)
        db.session.commit()
        return redirect('/')
    # Rendering everything out
    else:
        items = Expences.query.order_by(Expences.id).all()
        for item in items:
            if item.date_created.now().strftime("%Y-%m-%d") == datetime.now().strftime("%Y-%m-%d"):
                monthly_expences += item.price
        
        return render_template(
            'index.html',
            items=items, form=form,
            date = datetime.now(),
            monthly_expences = monthly_expences,)
    
    

@app.errorhandler(404)
def page_not_fount(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)