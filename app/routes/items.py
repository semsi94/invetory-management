from flask import Blueprint, request, jsonify
from app.models import Item, db

# Create a Blueprint object
items_bp = Blueprint('items', __name__)

# Define the /items route using the Blueprint
@items_bp.route('/items')
def items():
    items_data = [
        {"id": 1, "name": "Item 1", "price": "$10"},
        {"id": 2, "name": "Item 2", "price": "$15"},
        {"id": 3, "name": "Item 3", "price": "$20"}
    ]
    return jsonify({"items": items_data})
