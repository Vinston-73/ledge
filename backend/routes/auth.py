from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from auth.security import create_access_token, get_password_hashed, verify_password
from database.db import get_db
from models.userModel import User
from schema.user import userCreate

router = APIRouter(tags=["Auth"])
@router.post("/register")
def create_user(userSchema: userCreate, db: Session = Depends(get_db)):
  
    existing_user = db.query(User).filter(User.name == userSchema.name).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    existing_email = db.query(User).filter(User.email == userSchema.email).first()
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already registered")


    db_user = User(
        name=userSchema.name,
        email=userSchema.email,
        password=get_password_hashed(userSchema.password)
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {"message": "User created successfully", "user_id": db_user.id}
class LoginSchema(BaseModel):
    name: str
    password: str

@router.post("/login")
def login(data: LoginSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.name == data.name).first()
    if not user or not verify_password(data.password, user.password):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    access_token = create_access_token(data={"sub": user.name})
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": user.email
    }