"""create phone number for user column

Revision ID: b195d6e72fbf
Revises: 
Create Date: 2022-07-04 20:40:22.282189

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b195d6e72fbf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users', sa.Column("phone_number", sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column('users', "phone_number")
