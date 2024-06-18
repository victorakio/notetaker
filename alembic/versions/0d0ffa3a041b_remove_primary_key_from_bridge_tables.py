"""remove primary key from bridge tables

Revision ID: 0d0ffa3a041b
Revises: 84aae68facb0
Create Date: 2024-06-14 00:00:06.631100

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0d0ffa3a041b'
down_revision = '84aae68facb0'
branch_labels = None
depends_on = None

def upgrade():
    op.drop_constraint('PRIMARY', 'note_category', type_='primary')
    op.alter_column('note_category', 'note_id', existing_type=sa.Integer(), nullable=False)
    op.alter_column('note_category', 'category_id', existing_type=sa.Integer(), nullable=False)
    op.create_unique_constraint('uq_note_category', 'note_category', ['note_id', 'category_id'])

def downgrade():
    op.drop_constraint('uq_note_category', 'note_category', type_='unique')
    op.alter_column('note_category', 'note_id', existing_type=sa.Integer(), nullable=True)
    op.alter_column('note_category', 'category_id', existing_type=sa.Integer(), nullable=True)
    op.create_primary_key('PRIMARY', 'note_category', ['note_id', 'category_id'])