from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.dashboard.models import Expences, MonthlyExps
from app.dashboard.forms import AddExpenceForm
from datetime import datetime, timedelta
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
    if form.validate_on_submit():
        new_item = Expences(category=form.category_select.data, product=form.product_name.data, price=form.price_value.data, user=current_user.id)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('dashboard.dashboard'))
    # Rendering everything out
    else:
        items = Expences.query.filter_by(user=current_user.id).order_by(Expences.date_created.desc()).all()
        exps = MonthlyExps.query.filter_by(user=current_user.id).first()
        date = datetime.now()
        for item in items:
            if item.date_created.now().strftime("%Y-%m-%d") == datetime.now().strftime("%Y-%m-%d") and exps.date_updated.now().strftime("%Y-%m-%d") != datetime.now().strftime("%Y-%m-%d"):
                exps.monthly_expences += item.price
            if item.date_created.now().strftime("%Y-%m-%d") == datetime.now().strftime("%Y-%m-%d") and exps.date_updated.now().strftime("%Y-%m-%d") == datetime.now().strftime("%Y-%m-%d"):
                exps.previous_month_exps = exps.monthly_expences
                exps.monthly_expences = 0
                exps.monthly_expences += item.price
                exps.date_updated = datetime.utcnow()

        return render_template(
            'dashboard/dashboard.html',
            items=items, exps=exps, form=form,
            date = date,
            prev_month = date.today().replace(day=1) - timedelta(days=1)
            )