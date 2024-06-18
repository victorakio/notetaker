from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from backend.database import Base
from backend.models.note_category import note_category

class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    slug = Column(String(120), unique=True, index=True)
    user = Column(Integer, ForeignKey("users.id"))
    notes = relationship("Note", secondary=note_category, back_populates="categories")
