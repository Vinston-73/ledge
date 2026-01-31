
from backend.database.db import get_db
import models, schemas
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException

def create_user(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(models.user).offset(skip).limit(limit).all()
    return users


def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.Item).filter(models.user.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return user


def update_user(user_id: int,user: schemas.userCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.user).filter(models.user.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="Item not found")

    for field, value in user.dict().users():
        setattr(db_user, field, value)

    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.user).filter(models.user.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(user)
    db.commit()
    return {"message": "Item deleted successfully"}