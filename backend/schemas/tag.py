from pydantic import BaseModel

class TagBase(BaseModel):
    title: str
    slug: str

class TagCreate(TagBase):
    pass

class Tag(TagBase):
    id: int

    class Config:
        from_attributes = True