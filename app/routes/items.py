# app/routes/items.py
from flask import Blueprint, request, jsonify
from app.models import Item, db

# Create a Blueprint object with a unique name
items_bp = Blueprint('unique_items_blueprint', __name__, url_prefix='/items')

# Define the /items route using the Blueprint
@items_bp.route('/')
def items_home():
   return "Items home page"
    
@items_bp.route('/', methods=['GET'])
def get_items():
    items = Item.query.all()  # Retrieve all items from the database
    return jsonify([{'id': item.id, 'name': item.name, 'quantity': item.quantity, 'category_id': item.category_id} for item in items])

@items_bp.route('/', methods=['POST'])
def add_item():
    data = request.json  # Get data from the request body
    item = Item(name=data['name'], quantity=data['quantity'], category_id=data['category_id'])
    db.session.add(item)
    db.session.commit()  # Save to the database
    return jsonify({'message': 'Item added successfully'}), 201
