"""Add weather model

Revision ID: 8ca46bd21362
Revises: cbb8921272c8
Create Date: 2020-07-12 16:33:06.141605

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ca46bd21362'
down_revision = 'cbb8921272c8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('weather_forecasts', sa.Column('description', sa.String(length=50), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('weather_forecasts', 'description')
    # ### end Alembic commands ###
