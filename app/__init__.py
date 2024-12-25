from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configuration for SQLAlchemy
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'  # Change as needed
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize SQLAlchemy with the app
    db.init_app(app)

    return app
