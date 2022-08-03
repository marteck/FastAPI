"""Create address table

Revision ID: 423335c9e636
Revises: b195d6e72fbf
Create Date: 2022-07-16 18:38:27.034544

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '423335c9e636'
down_revision = 'b195d6e72fbf'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('address',
                    sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('address1', sa.String(), nullable=False),
                    sa.Column('address2', sa.String(), nullable=False),
                    sa.Column('city', sa.String(), nullable=False),
                    sa.Column('state', sa.String(), nullable=False),
                    sa.Column('country', sa.String(), nullable=False),
                    sa.Column('postal_code', sa.String(), nullable=False)
                    )


def downgrade() -> None:
    op.drop_table('address')
