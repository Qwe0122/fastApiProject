"""add column

Revision ID: 5aa6684ec53e
Revises: 
Create Date: 2024-11-01 12:23:48.997401

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5aa6684ec53e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column('name', sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'name')
