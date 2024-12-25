from flask import Blueprint, jsonify

# Create a Blueprint object
items_bp = Blueprint('items', __name__)

# Mock data
mock_items = [
    {"id": 1, "name": "Item 1", "quantity": 10, "category_id": 1},
    {"id": 2, "name": "Item 2", "quantity": 5, "category_id": 2},
    {"id": 3, "name": "Item 3", "quantity": 20, "category_id": 1}
]

# Define the /items route using the Blueprint
@items_bp.route('/')
def items_home():
    return "Items home page"
    
@items_bp.route('/items', methods=['GET'])
def get_items():
    # Return mock data as JSON
    return jsonify(mock_items)

@items_bp.route('/', methods=['POST'])
def add_item():
    # You can simulate adding an item with mock data
    new_item = {"id": len(mock_items) + 1, "name": "New Item", "quantity": 1, "category_id": 1}
    mock_items.append(new_item)
    return jsonify({'message': 'Item added successfully', 'item': new_item}), 201
