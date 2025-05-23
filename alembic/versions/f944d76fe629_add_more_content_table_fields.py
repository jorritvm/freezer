"""add more content table fields

Revision ID: f944d76fe629
Revises: 9cad6e462d78
Create Date: 2025-03-17 21:06:22.207266

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = 'f944d76fe629'
down_revision: Union[str, None] = '9cad6e462d78'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('freezercontent', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
        batch_op.add_column(sa.Column('article', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
        batch_op.add_column(sa.Column('add_date', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
        batch_op.add_column(sa.Column('comment', sqlmodel.sql.sqltypes.AutoString(), nullable=False))

    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('freezercontent', schema=None) as batch_op:
        batch_op.drop_column('comment')
        batch_op.drop_column('add_date')
        batch_op.drop_column('article')
        batch_op.drop_column('category')

    # ### end Alembic commands ###
