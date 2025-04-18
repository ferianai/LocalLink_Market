from instance.database import db
from datetime import datetime
from shared import crono


class OrderItem(db.Model):
    """OrderItem model for the application."""

    __tablename__ = "order_items"

    id: int = db.Column(db.Integer, primary_key=True)
    order_id: int = db.Column(db.Integer, db.ForeignKey("orders.id"), nullable=False)
    product_id: int = db.Column(
        db.Integer, db.ForeignKey("products.id"), nullable=False
    )
    quantity: int = db.Column(db.Integer, nullable=False)
    unit_price: str = db.Column(
        db.Numeric(10, 2), nullable=False
    )  # Decimal or String type
    created_at: datetime = db.Column(db.DateTime(timezone=True), default=crono.now)

    # Relationships
    order = db.relationship("Order", back_populates="order_items")
    product = db.relationship("Product", back_populates="order_items")

    def __repr__(self):
        return f"<OrderItem {self.id} for Order {self.order_id}>"
