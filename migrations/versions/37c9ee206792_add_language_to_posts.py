"""add language to posts

Revision ID: 37c9ee206792
Revises: 19e89b2a1e0d
Create Date: 2020-04-02 09:27:57.126960

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37c9ee206792'
down_revision = '19e89b2a1e0d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
