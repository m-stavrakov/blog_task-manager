from flask import Flask, render_template, Blueprint, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager, current_user
from .models import User, DiaryEntry, db
from werkzeug.security import check_password_hash, generate_password_hash

# initiating db
# db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__, static_folder='static')
    app.config.from_object('config')
    

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    with app.app_context():
        db.init_app(app)
        db.create_all()

    # where the user will be redirected if they have not logged in
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    return app