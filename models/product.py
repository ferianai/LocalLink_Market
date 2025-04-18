from instance.database import db
from datetime import datetime
from shared import crono


class Product(db.Model):
    """Product model representing items sold by vendors."""

    __tablename__ = "products"

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(150), nullable=False)
    description: str = db.Column(db.Text, nullable=True)
    price: float = db.Column(db.Numeric(10, 2), nullable=False)
    stock_quantity: int = db.Column(db.Integer, nullable=False)
    image_url: str = db.Column(db.String(255), nullable=True)
    location: str = db.Column(db.String(255), nullable=True)
    featured: bool = db.Column(db.Boolean, default=False)
    vendor_id: int = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    created_at: datetime = db.Column(db.DateTime, default=crono.now)
    updated_at: datetime = db.Column(db.DateTime, default=crono.now, onupdate=crono.now)

    # Relationships
    cart_items = db.relationship("CartItem", backref="product", lazy=True)
    order_items = db.relationship("OrderItem", backref="product", lazy=True)
    feedback = db.relationship("Feedback", backref="product", lazy=True)
    product_categories = db.relationship(
        "ProductCategory", backref="product", lazy=True
    )

    # repr method for better debugging
    def __repr__(self):
        return f"<Product {self.name}>"
