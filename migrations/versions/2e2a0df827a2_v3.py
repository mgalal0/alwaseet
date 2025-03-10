"""v3

Revision ID: 2e2a0df827a2
Revises: 6a1d74ee91c2
Create Date: 2024-05-13 18:19:06.996960

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e2a0df827a2'
down_revision = '6a1d74ee91c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index('name')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index('name', ['name'], unique=True)

    # ### end Alembic commands ###
