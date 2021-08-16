from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.dashboard.models import Expences, MonthlyExps
from app.dashboard.forms import AddExpenceForm
from datetime import datetime, timedelta
from app import login_manager
from flask_login import login_required, current_user
from app.auth.models import User
from flask_babel import gettext

board = Blueprint('dashboard', __name__, url_prefix='/dashboard')

# Login manager user loader 
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Main dashboard route
@board.route('/', methods=['POST', 'GET'])
@login_required
def dashboard():
    form = AddExpenceForm()
    
    # Adding new items
    if form.validate_on_submit():
        new_item = Expences(category=form.category_select.data, product=form.product_name.data, price=form.price_value.data, user=current_user.id)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('dashboard.dashboard'))
    
    # Rendering everything out
    else:
        # Initializing db models
        page = request.args.get('page', 1, type=int)
        exps = Expences.query.filter_by(user=current_user.id).order_by(Expences.date_created.desc()).all()
        expences = Expences.query.filter_by(user=current_user.id).order_by(Expences.date_created.desc()).paginate(per_page=5, page=page, error_out=True)
        mon_exps = MonthlyExps.query.filter_by(user=current_user.id).first()
        
        # Calculating monthly expences
        monthly_expences = 0
        prev_month_exps = 0
        pprev_month = (datetime.utcnow().replace(day=1) - timedelta(days=1)).replace(day=1) - timedelta(days=1)

        exps_per_category = {
            'Продукты': 0,
            'Развлечения': 0,
            'Налоги': 0,
            'Путешествия': 0,
            'Животние': 0,
            'Одежда': 0,
            'Транспорт': 0,
            'Медицина': 0,
            'Непредвиденные расходы': 0,
        }

        for exp in exps:
            if exp.date_created.utcnow().strftime("%Y-%m") == datetime.utcnow().strftime("%Y-%m"):
                monthly_expences += exp.price
                exps_per_category[exp.category] += exp.price
            elif exp.date_created.utcnow().strftime("%Y-%m") != datetime.utcnow().strftime("%Y-%m") and exp.date_created.utcnow().strftime("%Y-%m") > pprev_month:
                prev_month_exps += exp.price
                
            if mon_exps.date_updated.strftime("%Y-%m-%d") < datetime.utcnow().strftime("%Y-%m-%d"):
                mon_exps.monthly_expences = monthly_expences
                mon_exps.previous_month_exps = prev_month_exps
                mon_exps.date_updated = datetime.utcnow()
        
        data = []
        for key in exps_per_category:
            if exps_per_category[key] != 0:
                data.append((key, exps_per_category[key]) )

        labels = [row[0] for row in data]
        values = [row[1] for row in data]

        # Rendering
        return render_template(
            'dashboard/dashboard.html',
            expences=expences, mon_exps=mon_exps, form=form,
            prev_month = datetime.today().replace(day=1) - timedelta(days=1),
            monthly_expences=monthly_expences,
            prev_month_exps=prev_month_exps,
            labels=labels, values=values,
            )