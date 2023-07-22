"""empty message

Revision ID: 6171c4caa71f
Revises: b536fdf7b905
Create Date: 2023-07-21 12:10:49.740621

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6171c4caa71f'
down_revision = 'b536fdf7b905'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('items', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###
