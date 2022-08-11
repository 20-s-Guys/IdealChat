

#First release model is defined at one File, But Lator I want to split these things. 

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String , TIMESTAMP
from sqlalchemy import func #func.now()를 위함
from sqlalchemy.orm import relationship

from .database import Base


class USER(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, index=True)
    user_type = ForeignKey("type.user_type")
    name = Column(String(40), unique=True, index=True, nullable = False)
    password = Column(String(30), nullable = False)
    is_active = Column(Boolean, default=True)

    items = relationship("temp", back_populates="user", nullable = True)
    
    type = relationship("type", back_populates="user", uselist=False)
    

class TYPE(Base):
    __tablename__ = "type"
    user_type = Column(Integer, primary_key = True)
    is_active = Column(Boolean, default = True, )
    is_blackcow = Column(TIMESTAMP , default = func.now() )
    create_at = Column(TIMESTAMP , default = func.now() )
    update_at = Column(TIMESTAMP , default = func.now() )

    user = relationship("user", back_populates="type") # many-to-one 관계의 참조 변수 uselist를 False로 지정




class TEMP(Base):
    __tablename__ = "temp"

    room_index = Column(Integer, primary_key=True, index=True)
    r_friends = Column(String(999), nullable = True)
    room_name = Column(String(99), nullable = False)
    create_at = Column(TIMESTAMP, default = func.now())

    #relationship
    items = relationship("chat", back_populates="temp", nullable = True)


class CHAT(Base):
    __tablename__ = "chat"
    chat_id = Column(Integer,primary_key = True, autoincreasement = True)
    room_index = Column(Integer,  ForeignKey("room_index"),autoincrement = True, nullable = False )
    friends = ForeignKey("temp.r_friends")
    chats = Column(String(9999), nullable = False)
    receiver = Column(Boolean , nullable = False , default = True)
    create_at = Column(TIMESTAMP , default = func.now() )
    update_at = Column(TIMESTAMP , default = func.now() )

    owner = relationship("temp", back_populates="chat")

