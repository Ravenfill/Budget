from flask import Blueprint, render_template, request, redirect
from app import db
from app.dashboard.models import Expences
from app.dashboard.forms import AddExpenceForm
from datetime import datetime
from app import login_manager
from flask_login import login_required, current_user
from app.auth.models import User

board = Blueprint('dashboard', __name__, url_prefix='/dashboard')

# Login manager user loader 
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Main dashboard route
@board.route('/', methods=['POST', 'GET'])
@login_required
def dashboard():
    monthly_expences = 0
    form = AddExpenceForm()
    # Adding new items
    if request.method == 'POST' and form.validate():
        item_category = form.category_select.data
        item_product = form.product_name.data
        item_price = form.price_value.data
        new_item = Expences(category=item_category, product=item_product, price=item_price, user=current_user.id)
        db.session.add(new_item)
        db.session.commit()
        return redirect('/')
    # Rendering everything out
    else:
        exps = Expences.query.order_by(Expences.date_created.desc()).all()
        items = []
        for item in exps:
            if item.date_created.now().strftime("%Y-%m-%d") == datetime.now().strftime("%Y-%m-%d") and item.user == current_user.id:
                monthly_expences += item.price
            if item.user == current_user.id:
                items.append(item)
        
        return render_template(
            'dashboard/dashboard.html',
            items=items, form=form,
            date = datetime.now(),
            monthly_expences = monthly_expences,
            )