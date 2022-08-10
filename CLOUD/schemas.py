
#Notice that SQLAlchemy models define attributes using =, and pass the type as a parameter to Column, like in:
#name = Column(String)
#while Pydantic models declare the types using :, the new type annotation syntax/type hints:
#name: str


from pydantic import BaseModel
from typing import Optional

class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: Optional[str]
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True