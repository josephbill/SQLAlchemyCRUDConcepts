"""add column to authors

Revision ID: a9fa83627097
Revises: 3f74ef67ad9d
Create Date: 2023-09-04 11:28:18.292599

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a9fa83627097'
down_revision: Union[str, None] = '3f74ef67ad9d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('authors', sa.Column('publishedbooks', sa.String, index=True, nullable=True))


def downgrade() -> None:
    op.drop_column("authors","publishedbooks")
