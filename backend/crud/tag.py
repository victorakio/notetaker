from sqlalchemy.orm import Session
from backend.models.tag import Tag
from backend.schemas.tag import TagCreate

def get_tag(db: Session, tag_slug: str):
    return db.query(Tag).filter(Tag.slug == tag_slug).first()

def get_tags(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Tag).offset(skip).limit(limit).all()

def create_tag(db: Session, tag: TagCreate):
    db_tag = Tag(title=tag.title, slug=tag.slug)  # Assigned slug attribute
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag