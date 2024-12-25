from flask import Flask, render_template
from app.routes.items import items_bp  # Import blueprint

def create_app():
    app = Flask(__name__)

    
    app.register_blueprint(items_bp, url_prefix='/items')

   
    @app.route('/')
    def home():
        return render_template('index.html')  

    return app
