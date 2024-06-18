from sqlalchemy.orm import Session, joinedload

from backend.models.note import Note
from backend.schemas.note import NoteCreate

from backend.models.category import Category
from backend.models.tag import Tag

from backend.models.note_category import note_category
from backend.models.note_tag import note_tag

def get_note(db: Session, note_slug: str):
    return db.query(Note).filter(Note.slug == note_slug).first()

def get_notes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Note).offset(skip).limit(limit).all()

def create_note(db: Session, note: NoteCreate):
    db_note = Note(
        title=note.title,
        slug=note.slug,
        body=note.body,
        user=note.user,
    )

        # Retrieve and associate categories if they exist
    if note.category_ids:
        categories = db.query(Category).filter(Category.id.in_(note.category_ids)).all()
        db_note.categories.extend(categories)
    
    # Retrieve and associate tags if they exist
    if note.tag_ids:
        tags = db.query(Tag).filter(Tag.id.in_(note.tag_ids)).all()
        db_note.tags.extend(tags)

    db.add(db_note)
    db.commit()
    db.refresh(db_note)

    db_note = db.query(Note).options(joinedload(Note.categories), joinedload(Note.tags)).filter(Note.id == db_note.id).first()

    return db_note