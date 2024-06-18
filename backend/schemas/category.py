from pydantic import BaseModel

class CategoryBase(BaseModel):
    title: str
    slug: str

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

    class Config:
        from_attributes = True