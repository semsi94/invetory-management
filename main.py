from app import create_app
from flask import Flask, jsonify
from app.routes.items import items_bp

app = create_app()

app.register_blueprint(items_bp, url_prefix='/items')

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
