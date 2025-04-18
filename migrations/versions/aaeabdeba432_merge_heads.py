"""merge heads

Revision ID: aaeabdeba432
Revises: 78d7d315f080, update_password_hash_length
Create Date: 2025-04-18 21:21:21.297823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aaeabdeba432'
down_revision = ('78d7d315f080', 'update_password_hash_length')
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
