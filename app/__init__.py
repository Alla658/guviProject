import os
from flask import Flask
from .config import Config
from .extensions import db, migrate, login_manager  # Import initialized extensions

def create_app():
    app = Flask(
        __name__,
        template_folder=os.path.abspath("templates")  # Ensure templates folder is correctly set
    )
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Import models to register them for migrations
    from .models import User

    # Register blueprints (routes)
    from .routes import main
    from .auth import auth  # Ensure auth routes are included

    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app
