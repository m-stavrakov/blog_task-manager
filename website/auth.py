from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
import re

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        # Check if the User exists
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template('login.html', user = current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Email already exists!', category='error')
        elif len(email) < 5:
            flash('Email must be greater than 5 characters!', category='error')
        elif len(first_name) < 2 and len(last_name) < 2:
            flash('Both first name and last name must be greater than 2 characters!', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match!', category='error')
        elif len(password1) < 7 or not re.search(r'[A-Z]', password1) or not re.search(r'[^a-zA-Z0-9\s]', password1) or not re.search(r'\d', password1): 
            flash('Password must be at least 7 characters, it must contain one capital letter A-Z, one symbol and a number', category='error')
        else:
            # defining the user
            new_user = User(email=email, first_name=first_name, last_name = last_name, username = username, password = generate_password_hash(password1, method='pbkdf2:sha256'))

            # adding user to the db
            db.session.add(new_user)

            # committing to the db
            db.session.commit()

            login_user(new_user, remember=True)
            flash('Account created!', category='success')

            return redirect(url_for('views.home'))
    
    return render_template('signUp.html', user = current_user)
