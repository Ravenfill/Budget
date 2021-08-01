from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager, login_required, logout_user, current_user

# Base app creation
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.signup'

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

# Main routes
@app.route('/')
def index():
    return redirect(url_for('dashboard.dashboard'))

# GARBAGE
app.jinja_env.add_extension('jinja2.ext.loopcontrols')

db.create_all()