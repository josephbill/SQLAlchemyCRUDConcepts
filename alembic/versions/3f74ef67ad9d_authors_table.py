"""authors table

Revision ID: 3f74ef67ad9d
Revises: 
Create Date: 2023-09-04 11:25:24.716022

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3f74ef67ad9d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "authors",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("name", sa.String, index=True),
    )
 
def downgrade() -> None:
    op.drop_table("authors")

