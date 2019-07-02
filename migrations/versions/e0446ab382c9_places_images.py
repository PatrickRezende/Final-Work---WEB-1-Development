"""Places Images

Revision ID: e0446ab382c9
Revises: 83c7fdbac498
Create Date: 2019-06-25 09:57:44.709080

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0446ab382c9'
down_revision = '83c7fdbac498'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('places', sa.Column('image_name', sa.String(length=128), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('places', 'image_name')
    # ### end Alembic commands ###