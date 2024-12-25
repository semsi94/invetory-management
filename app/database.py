from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db():
    db.init_app(app)
    db.create_all()
