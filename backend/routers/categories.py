from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.schemas.category import Category, CategoryCreate
from backend.crud.category import get_category, create_category, get_categories
from backend.database import get_db

router = APIRouter()

@router.post("/categories/", response_model=Category)
def create_category_route(category: CategoryCreate, db: Session = Depends(get_db)):
    db_category = get_category(db, category_title=category.title)
    if db_category:
        raise HTTPException(status_code=400, detail="Category already registered")
    return create_category(db=db, category=category)

@router.get("/categories/{category_title}", response_model=Category)
def get_category_route(category_title: str, db: Session = Depends(get_db)):
    db_category = get_category(db, category_title=category_title)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category


@router.get("/categories/", response_model=list[Category])  # Changed the return type to a list of Tag
def get_categories_route(db: Session = Depends(get_db)):
    db_categories = get_categories(db)  # Updated to get_categories function
    if not db_categories:  # Check if the list is empty
        raise HTTPException(status_code=404, detail="Categories not found")
    return db_categories