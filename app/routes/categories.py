from flask import Blueprint, request, jsonify
from app.models import Category, db

categories_bp = Blueprint('categories', __name__)

@categories_bp.route('/', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return jsonify([{'id': category.id, 'name': category.name} for category in categories])

@categories_bp.route('/', methods=['POST'])
def add_category():
    data = request.json
    category = Category(name=data['name'])
    db.session.add(category)
    db.session.commit()
    return jsonify({'message': 'Category added successfully'}), 201
