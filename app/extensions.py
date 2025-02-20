from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt  # Added bcrypt
from flask import redirect, url_for

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
bcrypt = Bcrypt()  # Initialize bcrypt

from .models import User  # Import here to avoid circular import

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # Load user from DB

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('auth.login'))
