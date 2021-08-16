from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.auth.forms import SignInForm, SignUpForm
from app.auth.models import User
from app.dashboard.models import MonthlyExps
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from app import db
from flask_babel import gettext

auth = Blueprint('auth', __name__, url_prefix='/')

@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SignInForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user: 
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard.dashboard'))
            else:
                flash(gettext('Неверный пароль'))
        else:
            flash(gettext('Пользователь не зарегестрирован'))

    return render_template('/auth/signin.html', form=form)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        try:
            new_user = User(username=form.username.data, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=False)
            exps = MonthlyExps(user=new_user.id)
            db.session.add(exps)
            db.session.commit()
            return redirect(url_for('dashboard.dashboard'))
        except:
            flash(gettext('Пользователь уже существует'))
    elif len(form.username.data) < 4:
        flash(gettext('Имя пользователя слишком короткое'))
    elif len(form.password.data) < 4:
        flash(gettext('Пароль'))
    return render_template('/auth/signup.html', form=form)

@auth.route('/signout')
@login_required
def signout():
    logout_user()
    return redirect(url_for('auth.signin'))