from instance.database import db
from datetime import datetime
from shared import crono


class Cart(db.Model):
    """Shopping cart associated with a user."""

    __tablename__ = "cart"

    id: int = db.Column(db.Integer, primary_key=True)
    user_id: int = db.Column(
        db.Integer, db.ForeignKey("users.id"), unique=True, nullable=False
    )
    created_at: datetime = db.Column(db.DateTime, default=crono.now)

    # Relationships
    items = db.relationship("CartItem", backref="cart", lazy=True)
