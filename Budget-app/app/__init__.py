from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)

from app.dashboard.controllers import dashboard

app.register_blueprint(dashboard)

from app.auth.controllers import auth

app.register_blueprint(auth)

@app.errorhandler(404)
def page_not_fount(e):
    return render_template('/errorcodes/404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/')
def index():
    return redirect('/dashboard')

app.jinja_env.add_extension('jinja2.ext.loopcontrols')

db.create_all()