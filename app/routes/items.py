from flask import Blueprint, render_template, request

items_bp = Blueprint('items', __name__)


@items_bp.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        item_name = request.form['item_name']
        item_quantity = request.form['item_quantity']
        item_price = request.form['item_price']

        return f"Item '{item_name}' added with quantity {item_quantity} and price {item_price}."
    
    return render_template('add_item.html')
