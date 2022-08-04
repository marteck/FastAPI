"""add apt_nub column

Revision ID: bb10e0da6df5
Revises: 82bf9729935c
Create Date: 2022-07-16 22:25:01.748366

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'bb10e0da6df5'
down_revision = '82bf9729935c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("address", sa.Column("apt_num", sa.Integer(), nullable=True))


def downgrade() -> None:
    op.drop_column("address", "apt_num")
