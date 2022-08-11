from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.USER).filter(models.USER.id == user_id).first()

#it will change by 
def get_user_by_email(db: Session, email: str):
    return db.query(models.USER).filter(models.USER.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.USER).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.USER_Create):
    fake_hashed_password = user.u_password + "notreallyhashed"
    db_user = models.USER(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_temp(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.TEMP).offset(skip).limit(limit).all()


def create_user_temp(db: Session, item: schemas.TEMP_Create, user_id: int):
    db_item = models.TEMP(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
