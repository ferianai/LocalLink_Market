from instance.database import db


class ProductCategory(db.Model):
    """Association table for many-to-many relationship between products and categories."""

    __tablename__ = "product_categories"

    product_id: int = db.Column(
        db.Integer, db.ForeignKey("products.id"), primary_key=True
    )
    category_id: int = db.Column(
        db.Integer, db.ForeignKey("categories.id"), primary_key=True
    )
