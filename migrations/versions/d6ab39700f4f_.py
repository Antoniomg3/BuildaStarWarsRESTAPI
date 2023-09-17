"""empty message

Revision ID: d6ab39700f4f
Revises: 23cf4ca641cf
Create Date: 2022-11-15 17:12:45.089304

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd6ab39700f4f'
down_revision = '23cf4ca641cf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('favorites', 'name_favorites')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('favorites', sa.Column('name_favorites', mysql.VARCHAR(length=250), nullable=False))
    # ### end Alembic commands ###