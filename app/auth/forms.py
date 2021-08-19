from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length
from flask_babel import lazy_gettext

class SignInForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=16)], render_kw={"placeholder": lazy_gettext('Логин')})
    password = PasswordField('password', validators=[InputRequired(), Length(min=4, max=80)], render_kw={"placeholder": lazy_gettext('Пароль')})
    remember = BooleanField('Remember me', default=False)

class SignUpForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=16)], render_kw={"placeholder": lazy_gettext('Логин')})
    password = PasswordField('password', validators=[InputRequired(), Length(min=4, max=80)], render_kw={"placeholder": lazy_gettext('Пароль')})
    re_password = PasswordField('password', validators=[InputRequired(), Length(min=4, max=80)], render_kw={"placeholder": lazy_gettext('Повторите пароль')})