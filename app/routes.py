# -*- encoding: utf-8 -*-
# from flask import Flask

from app import app
# from templates import blueprint
from flask import render_template, redirect, url_for, request
# from flask_login import login_required, current_user
# from app import login_manager
from jinja2 import TemplateNotFound


# Pour formulaire
#from app import db, login_manager
#from app.base import blueprint
from app.forms import LoginForm, CreateAccountForm
#from app.base.models import User
from app.utils.util import verify_pass

# page d'acceuil
@app.route('/')
def index():
    login_form = LoginForm(request.form)
    if 'login' in request.form:
        
        # read form data
        username = request.form['username']
        password = request.form['password']

        # Locate user
        # user = User.query.filter_by(username=username).first()
        
        # Check the password
        # if user and verify_pass( password, user.password):

            # login_user(user)
            # return redirect(url_for('base_blueprint.route_default'))

        # Something (user or pass) is not ok
    return render_template( 'views/accounts/login.html', msg='Wrong user or password', form=login_form)
    
# page des dépenses
@app.route('/depenses')
def depenses():
    return render_template('views/admin/depenses.htm')

# page des budgets
@app.route('/budgets')
def budgets():
    return render_template('views/admin/budgets.htm')

# page du login
@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm(request.form)
    if 'login' in request.form:
        
        # read form data
        username = request.form['username']
        password = request.form['password']

        # Locate user
        # user = User.query.filter_by(username=username).first()
        
        # Check the password
        # if user and verify_pass( password, user.password):

            # login_user(user)
            # return redirect(url_for('base_blueprint.route_default'))

        # Something (user or pass) is not ok
    return render_template( 'views/accounts/login.html', msg='Wrong user or password', form=login_form)

    # if not current_user.is_authenticated:
        # return render_template( 'accounts/login.html',
                                # form=login_form)
    # return redirect(url_for('home_blueprint.index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    login_form = LoginForm(request.form)
    create_account_form = CreateAccountForm(request.form)
    if 'register' in request.form:

        username  = request.form['username']
        email     = request.form['email'   ]

        # Check usename exists
        # user = User.query.filter_by(username=username).first()
        # if user:
            # return render_template( 'accounts/register.html', 
                                    # msg='Username already registered',
                                    # success=False,
                                    # form=create_account_form)

        # Check email exists
        # user = User.query.filter_by(email=email).first()
        # if user:
            # return render_template( 'accounts/register.html', 
                                    # msg='Email already registered', 
                                    # success=False,
                                    # form=create_account_form)
# 
        # else we can create the user
        # user = User(**request.form)
        # db.session.add(user)
        # db.session.commit()
# 
        # return render_template( 'accounts/register.html', 
                                # msg='User created please <a href="/login">login</a>', 
                                # success=True,
                                # form=create_account_form)
# 
    # else:
    return render_template( 'views/accounts/register.html', form=create_account_form)

# @app.route('/logout')
# def logout():
    # logout_user()
    # return redirect(url_for('base_blueprint.login'))


# page du register
@app.route('/dashboard')
def dashboard():
   return render_template('index.htm')


# Outil pour tester les routes
with app.test_request_context():
    print(url_for('index'))
