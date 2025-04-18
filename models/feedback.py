from instance.database import db
from datetime import datetime
from shared import crono


class Feedback(db.Model):
    """Feedback model for the application."""

    __tablename__ = "feedback"

    id: int = db.Column(db.Integer, primary_key=True)
    user_id: int = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    product_id: int = db.Column(
        db.Integer, db.ForeignKey("products.id"), nullable=False
    )
    rating: int = db.Column(db.Integer, nullable=False)
    comment: str = db.Column(db.Text, nullable=True)
    created_at: datetime = db.Column(db.DateTime(timezone=True), default=crono.now)

    # Relationships
    user = db.relationship("User", backref="feedback")
    product = db.relationship("Product", backref="feedback")

    def __repr__(self):
        return (
            f"<Feedback {self.id} for Product {self.product_id} by User {self.user_id}>"
        )
