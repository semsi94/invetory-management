from flask import Blueprint, request, jsonify
from app.models import Item
from app import db

# Create a Blueprint object
items_bp = Blueprint('items', __name__)

# Define the /items route using the Blueprint
@items_bp.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()  # Ensure database is set up
    return jsonify([{'id': item.id, 'name': item.name, 'quantity': item.quantity, 'category_id': item.category_id} for item in items])

@items_bp.route('/items', methods=['POST'])
def add_item():
    data = request.json
    item = Item(name=data['name'], quantity=data['quantity'], category_id=data['category_id'])
    db.session.add(item)
    db.session.commit()
    return jsonify({'message': 'Item added successfully'}), 201
