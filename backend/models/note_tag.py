from sqlalchemy import Table, Column, Integer, ForeignKey
from backend.database import Base

note_tag = Table(
    'note_tag', Base.metadata,
    Column('note_id', Integer, ForeignKey('notes.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True)
)