from sqlalchemy import Table, Column, Integer, ForeignKey
from backend.database import Base

note_category = Table(
    'note_category', Base.metadata,
    Column('note_id', Integer, ForeignKey('notes.id'), primary_key=True),
    Column('category_id', Integer, ForeignKey('categories.id'), primary_key=True)
)