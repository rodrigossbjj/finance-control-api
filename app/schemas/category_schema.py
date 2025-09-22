from pydantic import BaseModel

class CategoryBase(BaseModel):
    name: str
    description: str | None = None

class CategoryCreate(CategoryBase):
    user_id: int | None = None   
    
class CategoryUpdate(CategoryBase):
    pass

class CategoryOut(CategoryBase):
    id: int
    user_id: int | None = None   

    class Config:
        orm_mode = True
