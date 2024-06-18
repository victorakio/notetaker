from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from backend.database import Base
from backend.models.note_tag import note_tag

class Tag(Base):
    __tablename__ = "tags"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    slug = Column(String(120), unique=True, index=True)
    notes = relationship("Note", secondary=note_tag, back_populates="tags")
    user = Column(Integer, ForeignKey("users.id"))