from instance.database import db
from datetime import datetime
from shared import crono


class CartItem(db.Model):
    """Items in a user's cart."""

    __tablename__ = "cart_items"

    id: int = db.Column(db.Integer, primary_key=True)
    cart_id: int = db.Column(db.Integer, db.ForeignKey("cart.id"), nullable=False)
    product_id: int = db.Column(
        db.Integer, db.ForeignKey("products.id"), nullable=False
    )
    quantity: int = db.Column(db.Integer, nullable=False)
    added_at: datetime = db.Column(db.DateTime, default=crono.now)
