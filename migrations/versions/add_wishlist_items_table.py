"""Add wishlist_items table

Revision ID: add_wishlist_items_table
Revises: aaeabdeba432
Create Date: 2025-04-18 22:00:00.000000

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "add_wishlist_items_table"
down_revision = "aaeabdeba432"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "wishlist_items",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("product_id", sa.Integer(), nullable=False),
        sa.Column("added_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.ForeignKeyConstraint(
            ["product_id"],
            ["products.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade():
    op.drop_table("wishlist_items")
