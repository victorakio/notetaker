from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.schemas.tag import Tag, TagCreate
from backend.crud.tag import get_tag, create_tag, get_tags
from backend.database import get_db
from backend.utils.auth import get_current_user
from backend.schemas.user import User

router = APIRouter()

@router.post("/tags/", response_model=Tag)
def create_tag_route(tag: TagCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_tag = get_tag(db, tag_slug=tag.title)
    if db_tag:
        raise HTTPException(status_code=400, detail="Tag already registered")
    return create_tag(db=db, tag=tag)

@router.get("/tags/{tag_slug}", response_model=Tag)  # Changed the path parameter name
def get_tag_route(tag_slug: str, db: Session = Depends(get_db)):
    db_tag = get_tag(db, tag_slug=tag_slug)
    if db_tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return db_tag

@router.get("/tags/", response_model=list[Tag])  # Changed the return type to a list of Tag
def get_tags_route(db: Session = Depends(get_db)):
    db_tags = get_tags(db)  # Updated to get_tags function
    if not db_tags:  # Check if the list is empty
        raise HTTPException(status_code=404, detail="Tags not found")
    return db_tags