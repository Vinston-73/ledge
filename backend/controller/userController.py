
from models import userModel
from database.db import get_db
from schemas.userSchema import CreateUser
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException

def create_user(user:CreateUser, db: Session = Depends(get_db)):
    db_user = userModel.user(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = db.query(userModel.user).offset(skip).limit(limit).all()
#     return users


# def read_user(user_id: int, db: Session = Depends(get_db)):
#     user = db.query(userModel.user).filter(userModel.user.id == user_id).first()
#     if user is None:
#         raise HTTPException(status_code=404, detail="user not found")
#     return user


# def update_user(user_id: int,user: create_user, db: Session = Depends(get_db)):
#     db_user = db.query(userModel.user).filter(userModel.user.id == user_id).first()
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="user not found")

#     for field, value in user.dict().users():
#         setattr(db_user, field, value)

#     db.commit()
#     db.refresh(db_user)
#     return db_user


def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(userModel.user).filter(userModel.user.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="user not found")

    db.delete(user)
    db.commit()
    return {"message": "user deleted successfully"}