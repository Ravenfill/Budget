from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length

class SignInForm(Form):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=16)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=4, max=80)])
    remember = BooleanField('Remember me', default=False)

class SignUpForm(Form):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=16)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=4, max=80)])