"""Initial migration 3

Revision ID: df98318dfce3
Revises: b0af3832a8b7
Create Date: 2020-07-07 22:53:54.004569

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df98318dfce3'
down_revision = 'b0af3832a8b7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('availabledates',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_', sa.String(length=50), nullable=True),
    sa.Column('tour_date', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['tour_date'], ['tourpackage.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('available_dates')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('available_dates',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('date_', sa.VARCHAR(length=50), nullable=True),
    sa.Column('tour_date', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['tour_date'], ['tourpackage.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('availabledates')
    # ### end Alembic commands ###
