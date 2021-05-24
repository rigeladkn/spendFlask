# -*- encoding: utf-8 -*-
from flask import Flask
app = Flask(__name__)
# from templates import blueprint
from flask import render_template, redirect, url_for, request
# from flask_login import login_required, current_user
# from app import login_manager
from jinja2 import TemplateNotFound

# page d'acceuil
@app.route('/')
def index():
    return render_template('index.htm')

# page des dépenses
@app.route('/depenses')
def depenses():
    return render_template('views/admin/depenses.htm')

# page des budgets
@app.route('/budgets')
def budgets():
    return render_template('views/admin/budgets.htm')



# Outil pour tester les routes
with app.test_request_context():
    print(url_for('index'))
