
#Notice that SQLAlchemy models define attributes using =, and pass the type as a parameter to Column, like in:
#name = Column(String)
#while Pydantic models declare the types using :, the new type annotation syntax/type hints:
#name: str


from pydantic import BaseModel
from typing import Optional

class TEMP_Base(BaseModel):
    title: str
    description: str | None = None


class TEMP_Create(TEMP_Base):
    pass


class TEMP(TEMP_Base):
    id: Optional[str]
    owner_id: int

    class Config:
        orm_mode = True


class USER_Base(BaseModel):
    email: str


class USER_Create(USER_Base):
    u_password: str


class USER(USER_Base):
    id: int
    is_active: bool
    items: list[TEMP] = []

    class Config:
        orm_mode = True