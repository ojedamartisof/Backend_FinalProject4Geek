"""empty message

Revision ID: fc0e20b62ea1
Revises: fc84484c8e97
Create Date: 2020-12-07 10:57:55.221372

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'fc0e20b62ea1'
down_revision = 'fc84484c8e97'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'firstname',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
    op.alter_column('user', 'lastname',
               existing_type=mysql.VARCHAR(length=100),
               nullable=False)
    op.drop_column('user', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password_hash', mysql.VARCHAR(length=100), nullable=True))
    op.alter_column('user', 'lastname',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
    op.alter_column('user', 'firstname',
               existing_type=mysql.VARCHAR(length=100),
               nullable=True)
    # ### end Alembic commands ###