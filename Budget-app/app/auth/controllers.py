from flask import Blueprint, render_template, request, redirect

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/')
def index():
    return render_template('/auth/authorization.html')