"""empty message

Revision ID: cf518497bb43
Revises: 8b40144a3f48
Create Date: 2022-03-05 18:52:22.415255

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf518497bb43'
down_revision = '8b40144a3f48'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cuboids', sa.Column('volume', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cuboids', 'volume')
    # ### end Alembic commands ###
