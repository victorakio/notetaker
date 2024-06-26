from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.schemas.category import Category, CategoryCreate
from backend.crud.category import get_category, create_category, get_categories
from backend.database import get_db
from backend.utils.auth import get_current_user
from backend.schemas.user import User

router = APIRouter()

@router.post("/categories/", response_model=Category)
def create_category_route(
    category: CategoryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)  # Ensure get_current_user is imported correctly
):
    db_category = get_category(db, category_slug=category.title)
    if db_category:
        raise HTTPException(status_code=400, detail="Category already registered")
    return create_category(db=db, category=category)

@router.get("/categories/{category_slug}", response_model=Category)
def get_category_route(category_slug: str, db: Session = Depends(get_db)):
    db_category = get_category(db, category_slug=category_slug)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category


@router.get("/categories/", response_model=list[Category])  # Changed the return type to a list of Tag
def get_categories_route(db: Session = Depends(get_db)):
    db_categories = get_categories(db)  # Updated to get_categories function
    if not db_categories:  # Check if the list is empty
        raise HTTPException(status_code=404, detail="Categories not found")
    return db_categories