from flask import Flask
from app.routes.items import items_bp

def create_app():
    app = Flask(__name__)


    app.register_blueprint(items_bp, url_prefix='/items')


    @app.route('/')
    def home():
        return "Welcome to the Inventory Management System!"

    return app
