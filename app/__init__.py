from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager
from flask_moment import Moment
from flask_babel import Babel

# Base app creation
app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.signup'

moment = Moment(app)

babel = Babel(app)


# Blueprints registration
from app.dashboard.controllers import board
app.register_blueprint(board)

from app.auth.controllers import auth
app.register_blueprint(auth)

# Error handlers
@app.errorhandler(404)
def page_not_fount(e):
    return render_template('/errorcodes/404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.before_request
def make_session_permanent():
    session.permanent = False

# Babel locales
@babel.localeselector
def get_locale():
  return request.accept_languages.best_match(app.config['LANGUAGES'])
  #return 'uk'

# Main routes
@app.route('/')
def index():
    return redirect(url_for('dashboard.dashboard'))

# GARBAGE
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

db.create_all()