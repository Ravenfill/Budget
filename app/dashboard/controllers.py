from flask import Blueprint, render_template, request, redirect, url_for, g, has_request_context
from app import db
from app.dashboard.models import Expences, MonthExpencesProfile
from app.dashboard.forms import AddExpenceForm
from datetime import datetime, timedelta
from app import login_manager
from flask_login import login_required, current_user
from app.auth.models import User

board = Blueprint('dashboard', __name__, url_prefix='/<lang_code>')

@board.url_defaults
def add_language_code(endpoint, values):
    values.setdefault('lang_code', g.lang_code)

@board.url_value_preprocessor
def pull_lang_code(endpoint, values):
    g.lang_code = values.pop('lang_code')

# Login manager user loader 
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Main dashboard route
@board.route('/')
@board.route('/dashboard', methods=['POST', 'GET'])
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
        
        # Calculating monthly expences
        monthly_expences = 0
        prev_month_exps = 0
        pprev_month = (datetime.utcnow().replace(day=1) - timedelta(days=1)).replace(day=1) - timedelta(days=1)

        exps_per_category = {
            'FOOD': 0,
            'ENTER': 0,
            'TAX': 0,
            'TRAVELS': 0,
            'PETS': 0,
            'CLOTHES': 0,
            'TRANS': 0,
            'MEDICINE': 0,
            'UNEXP': 0,
        }

        for exp in exps:
            if exp.date_created.utcnow().strftime("%Y-%m") == datetime.utcnow().strftime("%Y-%m"):
                monthly_expences += exp.price
                exps_per_category[exp.category] += exp.price
            elif exp.date_created.utcnow().strftime("%Y-%m") != datetime.utcnow().strftime("%Y-%m") and exp.date_created.utcnow().strftime("%Y-%m") > pprev_month:
                prev_month_exps += exp.price
        
        data = []
        for key in exps_per_category:
            if exps_per_category[key] != 0:
                data.append((key, exps_per_category[key]) )

        labels = [row[0] for row in data]
        values = [row[1] for row in data]

        # Rendering
        return render_template(
            'dashboard/dashboard.html',
            expences=expences, form=form,
            prev_month = datetime.today().replace(day=1) - timedelta(days=1),
            monthly_expences=monthly_expences,
            prev_month_exps=prev_month_exps,
            labels=labels, values=values,
            username = current_user.username,
            data = data,
            date = datetime.utcnow()
            )

@board.route('/profile')
def profile():

    data = MonthExpencesProfile()

    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    return render_template('dashboard/profile.html', labels=labels, values=values)

@board.route('/settings')
def settings():
    return render_template('dashboard/settings.html')