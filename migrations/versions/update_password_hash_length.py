"""Update password_hash length in users table

Revision ID: update_password_hash_length
Revises:
Create Date: 2025-04-18 21:05:00.000000

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "update_password_hash_length"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        "users",
        "password_hash",
        existing_type=sa.String(length=128),
        type_=sa.String(length=512),
        existing_nullable=False,
    )


def downgrade():
    op.alter_column(
        "users",
        "password_hash",
        existing_type=sa.String(length=512),
        type_=sa.String(length=128),
        existing_nullable=False,
    )
