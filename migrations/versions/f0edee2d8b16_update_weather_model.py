"""Update weather model

Revision ID: f0edee2d8b16
Revises: fda8915ef62b
Create Date: 2020-07-12 22:47:27.564443

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0edee2d8b16'
down_revision = 'fda8915ef62b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('weather_forecasts', 'date_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('weather_forecasts', sa.Column('date_time', sa.VARCHAR(length=50), nullable=True))
    # ### end Alembic commands ###
