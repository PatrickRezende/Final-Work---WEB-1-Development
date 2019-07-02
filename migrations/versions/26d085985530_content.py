"""Content

Revision ID: 26d085985530
Revises: a82c7061679c
Create Date: 2019-06-26 11:33:36.203093

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26d085985530'
down_revision = 'a82c7061679c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('story', sa.Column('content', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('story', 'content')
    op.add_column('places', sa.Column('content', sa.TEXT(), nullable=True))
    # ### end Alembic commands ###
