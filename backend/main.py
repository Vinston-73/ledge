from fastapi import FastAPI,Depends, HTTPException,APIRouter
from models import userModel
from schemas import userSchema
from controller import userController
from database.db import engine

from database.db import Base
from sqlalchemy.orm import Session
from database.db import get_db
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI()

Base.metadata.create_all(bind=engine)

app.add_middleware(CORSMiddleware,
    allow_origins=["https://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

router=APIRouter()
@router.post("/register/", response_model=userSchema.User)
def create_user(user: userSchema.CreateUser, db: Session = Depends(get_db)):
    return userController.create_user(user,db)

app.include_router(router)
# @router.get("/users/{user_id}", response_model=userSchema.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     user = db.query(user).filter(userModel.user.id == user_id).first()
#     if user is None:
#         raise HTTPException(status_code=404, detail="user not found")
#     return user

# @router.put("/users/{user_id}", response_model=userSchema.User)
# def update_user(user_id: int,user: userSchema.update_user, db: Session = Depends(get_db)):
#     db_user = db.query(userModel.user).filter(userModel.user.id == user_id).first()
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="user not found")

#     for field, value in user.dict().users():
#         setattr(db_user, field, value)

#     db.commit()
#     db.refresh(db_user)
#     return db_user

# @router.delete("/users/{user_id}")
# def delete_user(user_id: int, db: Session = Depends(get_db)):
#     user = db.query(userModel.user).filter(userModel.user.id == user_id).first()
#     if user is None:
#         raise HTTPException(status_code=404, detail="user not found")

#     db.delete(user)
#     db.commit()
#     return {"message": "user deleted successfully"}

