"""Feedbackrating change to item

Revision ID: ce13e3cd143e
Revises: 7540b4e774f2
Create Date: 2024-07-07 11:15:49.688084

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ce13e3cd143e'
down_revision: Union[str, None] = '7540b4e774f2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('feedback_ratings', sa.Column('feedback_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'feedback_ratings', type_='foreignkey')
    op.create_foreign_key('feedback_ratings_feedback_id_fkey', 'feedback_ratings', 'userFeedback', ['feedback_id'], ['id'])
    op.drop_constraint('unique_user_item', 'feedback_ratings', type_='unique')
    op.create_unique_constraint('unique_user_feedback', 'feedback_ratings', ['user_id', 'feedback_id'])
    op.drop_column('feedback_ratings', 'item_id')
    op.create_table('userFeedback',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='userFeedback_pkey'),
    sa.UniqueConstraint('title', name='userFeedback_title_key')
    )
    # ### end Alembic commands ###
