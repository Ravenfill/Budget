from flask import Blueprint, render_template, request, redirect, url_for, g
from app import db
from app.dashboard.models import Expences, MonthlyExps
from app.dashboard.forms import AddExpenceForm
from datetime import datetime, timedelta
from app import login_manager
from flask_login import login_required, current_user
from app.auth.models import User
from flask_babel import gettext

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
            'Питомцы': 0,
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
            username = current_user.username
            )

@board.route('/profile')
def profile():

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

    exps = Expences.query.filter_by(user=current_user.id).order_by(Expences.date_created.desc()).all()

    for exp in exps:
        if exp.date_created.utcnow().strftime("%Y-%m") == first_date.strftime("%Y-%m"):
            first_exps += exp.price
        elif exp.date_created.utcnow().strftime("%Y-%m") == second_date.strftime("%Y-%m"):
            second_exps += exp.price
        elif exp.date_created.utcnow().strftime("%Y-%m") == third_date.strftime("%Y-%m"):
            third_exps += exp.price
        elif exp.date_created.utcnow().strftime("%Y-%m") == fourth_exps.strftime("%Y-%m"):
            fourth_exps += exp.price
        elif exp.date_created.utcnow().strftime("%Y-%m") == fifth_date.strftime("%Y-%m"):
            first_exps += exp.price

    exp_n = [first_exps, second_exps, third_exps, fourth_exps, fifth_exps]
    exp_d = [gettext(str(first_date.utcnow().strftime("%B"))), gettext(str(second_date.utcnow().strftime("%B"))), 
            gettext(str(third_date.utcnow().strftime("%B"))), gettext(str(fourth_date.utcnow().strftime("%B"))), 
            gettext(str(fifth_date.utcnow().strftime("%B")))]

    s_data = []
    for i in range(0, 5):
        if exp_n[i] != 0:
            s_data.append((exp_d[i], exp_n[i]))
    
    s_labels = [row[0] for row in s_data]
    s_values = [row[1] for row in s_data]

    return render_template('dashboard/profile.html', first_exps=first_exps, s_labels=s_labels, s_values=s_values, s_data=s_data)

@board.route('/settings')
def settings():
    return render_template('dashboard/settings.html')