from flask import Flask
from app.database import init_db

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    with app.app_context():
        init_db(app)

        from app.routes.items import items_bp
        from app.routes.categories import categories_bp

        app.register_blueprint(items_bp, url_prefix='/items')
        app.register_blueprint(categories_bp, url_prefix='/categories')

    return app
