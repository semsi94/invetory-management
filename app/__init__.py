from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'  # Example SQLite database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    
    from app.routes.items import items_bp  # Import the blueprint
    app.register_blueprint(items_bp)  # Register the blueprint

    return app
