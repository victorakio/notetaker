from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from backend.database import Base
from backend.models.note_category import note_category
from backend.models.note_tag import note_tag


class Note(Base):
    __tablename__ = "notes"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50))
    slug = Column(String(50), index=True)
    body = Column(String(120))
    user = Column(Integer, ForeignKey("users.id"))
    categories = relationship("Category", secondary=note_category, back_populates="notes")
    tags = relationship("Tag", secondary=note_tag, back_populates="notes")
    created_at = Column(DateTime, default=datetime.now)
