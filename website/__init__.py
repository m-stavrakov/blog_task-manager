from flask import Flask
import os
from flask_login import LoginManager
from .models import User, db

login_manager = LoginManager()

def create_app():
    app = Flask(__name__, static_folder='static')
    app.config.from_object('config')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgresql://martinstavrakov:password@localhost:5432/blog-tasks')
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    with app.app_context():
        db.create_all()

    # where the user will be redirected if they have not logged in
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    return app