from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.schemas.note import Note, NoteCreate
from backend.crud.note import get_note, create_note, get_notes
from backend.models.note import Note as NoteModel
from backend.models.category import Category as CategoryModel
from backend.models.tag import Tag as TagModel
from backend.database import get_db
from backend.schemas.category import Category
router = APIRouter()

@router.post("/notes/", response_model=Note)
def create_note_route(note: NoteCreate, db: Session = Depends(get_db)):
    db_note = get_note(db, note_slug=note.slug)
    if db_note:
        raise HTTPException(status_code=400, detail="Note already registered")
    return create_note(db=db, note=note)

@router.get("/notes/{note_slug}", response_model=Note)  # Changed the path parameter name
def get_note_route(note_slug: str, db: Session = Depends(get_db)):
    db_note = get_note(db, note_slug=note_slug)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note

@router.get("/notes/", response_model=list[Note])
def get_notes(category_id: int = None, tag_id: int = None, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    query = db.query(NoteModel)
    
    # Filter by category if category_id is provided
    if category_id is not None:
        query = query.join(NoteModel.categories).filter(CategoryModel.id == category_id)
            
    # Filter by category if tag_id is provided
    if tag_id is not None:
        query = query.join(NoteModel.tags).filter(TagModel.id == tag_id)
    
    notes = query.offset(skip).limit(limit).all()
    return notes