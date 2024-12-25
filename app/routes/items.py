from flask import Blueprint, request, jsonify
from app.models import Item, db

# Create a Blueprint object
items_bp = Blueprint('items', __name__)

@items_bp.route('/', methods=['GET'])
def get_items():
    items = Item.query.all()  # Replace with mock data if database isn't set up
    return jsonify([
        {'id': item.id, 'name': item.name, 'quantity': item.quantity, 'category_id': item.category_id}
        for item in items
    ])

@items_bp.route('/', methods=['POST'])
def add_item():
    data = request.json
    item = Item(name=data['name'], quantity=data['quantity'], category_id=data['category_id'])
    db.session.add(item)
    db.session.commit()
    return jsonify({'message': 'Item added successfully'}), 201

@items_bp.route('/check', methods=['GET'])
def check():
    return jsonify({"message": "Items blueprint is loaded and working!"})
