from flask import render_template
from flask_login import login_required
from .import bp as main
from app.blueprints.auth.models import User

@main.route('/', methods =['GET', 'POST'])
@login_required
def home():
    return render_template('home.html.j2')

@main.route('/market', methods =['GET'])
def market():
    return render_template('market.html.j2')