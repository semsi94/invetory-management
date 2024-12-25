from flask import Flask
from app.routes.items import items_bp

def create_app():
    app = Flask(__name__)

    # Register the blueprint for /items
    app.register_blueprint(items_bp, url_prefix='/items')

    # Define a route for the root URL (/)
    @app.route('/')
    def home():
        return "Welcome to the Inventory Management System!"

    return app
