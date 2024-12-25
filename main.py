from app import create_app
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    # Example JSON data
    data = {
        "message": "Welcome to the JSON API",
        "status": "success",
        "items": [
            {"id": 1, "name": "Item 1", "price": "$10"},
            {"id": 2, "name": "Item 2", "price": "$15"},
            {"id": 3, "name": "Item 3", "price": "$20"}
        ]
    }
    return jsonify(data)  # Return JSON data as response

@app.route('/items')
def items():
    # Example JSON data for items
    items_data = [
        {"id": 1, "name": "Item 1", "price": "$10"},
        {"id": 2, "name": "Item 2", "price": "$15"},
        {"id": 3, "name": "Item 3", "price": "$20"}
    ]
    return jsonify({"items": items_data})  # Return items as JSON

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

