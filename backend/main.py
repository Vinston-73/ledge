from fastapi import FastAPI,Depends, HTTPException,APIRouter
from database.db import engine
import models,crud, schemas
from sqlalchemy.orm import Session
from backend.database.db import get_db
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI()





models.Base.metadata.create_all(bind=engine)

app.add_middleware(CORSMiddleware,
    allow_origins=["https://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

router=APIRouter()
@router.post("/users/", response_model=schemas.user)
def create_user(user: schemas.userCreate, db: Session = Depends(get_db)):
    return crud.create_user(db,user)

@router.put("/users/{user_id}", response_model=schemas.user)
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(models.user).offset(skip).limit(limit).all()
    return users


@router.get("/users/{user_id}", response_model=schemas.user)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.user).filter(models.user.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="user not found")
    return user

@router.put("/users/{user_id}", response_model=schemas.user)
def update_user(user_id: int,user: schemas.userCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.user).filter(models.user.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="user not found")

    for field, value in user.dict().users():
        setattr(db_user, field, value)

    db.commit()
    db.refresh(db_user)
    return db_user

@router.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.user).filter(models.user.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="user not found")

    db.delete(user)
    db.commit()
    return {"message": "user deleted successfully"}

