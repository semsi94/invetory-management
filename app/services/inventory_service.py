from app.models import Item, db

class InventoryService:
    @staticmethod
    def update_item_quantity(item_id, quantity):
        item = Item.query.get(item_id)
        if not item:
            return {'error': 'Item not found'}, 404
        item.quantity = quantity
        db.session.commit()
        return {'message': 'Item quantity updated successfully'}
