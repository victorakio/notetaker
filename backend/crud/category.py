from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from backend.models.category import Category
from backend.schemas.category import CategoryCreate

def get_category(db: Session, category_slug: str):
    return db.query(Category).filter(Category.slug == category_slug).first()

def get_categories(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Category).offset(skip).limit(limit).all()

def create_category(db: Session, category: CategoryCreate):
  try:
    db_category = Category(**category.model_dump())  # Assigned slug attribute
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category
  except IntegrityError as e:
    db.rollback()
    raise HTTPException(status_code=400, detail="Tag with this slug already exists")