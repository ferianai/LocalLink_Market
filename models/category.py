from instance.database import db


class Category(db.Model):
    """Category model that supports hierarchical structure and vendor ownership."""

    __tablename__ = "categories"

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(100), nullable=False)
    description: str = db.Column(db.Text, nullable=True)
    vendor_id: int = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    parent_id: int = db.Column(
        db.Integer, db.ForeignKey("categories.id"), nullable=True
    )

    # Relationships
    children = db.relationship(
        "Category", backref=db.backref("parent", remote_side=[id])
    )
    product_categories = db.relationship(
        "ProductCategory", backref="category", lazy=True
    )
