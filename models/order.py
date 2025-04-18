from instance.database import db
from datetime import datetime
import enum
from sqlalchemy.sql import func
from shared import crono


class OrderStatus(enum.Enum):
    pending = "pending"
    processing = "processing"
    shipped = "shipped"
    delivered = "delivered"
    cancelled = "cancelled"


class Order(db.Model):
    """Order model for the application."""

    __tablename__ = "orders"

    id: int = db.Column(db.Integer, primary_key=True)
    user_id: int = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    total_amount: str = db.Column(
        db.Numeric(10, 2), nullable=False
    )  # Decimal or String type
    status: OrderStatus = db.Column(
        db.Enum(OrderStatus), default=OrderStatus.pending, nullable=False
    )
    created_at: datetime = db.Column(db.DateTime(timezone=True), default=crono.now)

    # Relationships
    user = db.relationship("Users", back_populates="orders")
    order_items = db.relationship(
        "OrderItem", back_populates="order", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Order {self.id} by User {self.user_id}>"
