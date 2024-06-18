from pydantic import BaseModel
from typing import Optional, List

from backend.schemas.category import Category
from backend.schemas.tag import Tag

class NoteBase(BaseModel):
    title: str
    slug: str
    body: str
    user: int
    category_ids: Optional[List[int]] = []
    tag_ids: Optional[List[int]] = []

class NoteCreate(NoteBase):
    pass

class NoteInDB(NoteBase):
    id: int

class Note(NoteInDB):
    categories: List[Category] = []
    tags: List[Tag] = []

    class Config:
        from_attributes = True

class NoteResponse(Note):
    pass