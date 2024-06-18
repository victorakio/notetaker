from sqlalchemy.orm import Session
from backend.models.category import Category
from backend.schemas.category import CategoryCreate

def get_category(db: Session, category_title: str):
    return db.query(Category).filter(Category.title == category_title).first()

def get_categories(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Category).offset(skip).limit(limit).all()

def create_category(db: Session, category: CategoryCreate):
    db_category = Category(title=category.title, slug=category.slug)  # Assigned slug attribute
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category