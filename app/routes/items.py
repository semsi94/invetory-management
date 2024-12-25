from flask import Blueprint

items_bp = Blueprint('items', __name__)

# Root route for /items/
@items_bp.route('/')
def items_home():
    return "Welcome to the Items Section!"

# You can add other routes here related to items...
@app.route('/')
def home():
    return "Welcome to the Inventory Management System!"
