from instance.database import db
from datetime import datetime
from shared import crono


class WishlistItem(db.Model):
    """Wishlist items saved by users."""

    __tablename__ = "wishlist_items"

    id: int = db.Column(db.Integer, primary_key=True)
    user_id: int = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    product_id: int = db.Column(
        db.Integer, db.ForeignKey("products.id"), nullable=False
    )
    added_at: datetime = db.Column(db.DateTime, default=crono.now)

    user = db.relationship("Users", backref="wishlist_items", lazy=True)
    product = db.relationship("Product", backref="wishlist_items", lazy=True)
