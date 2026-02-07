from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database.db import get_db
from schema.user import UserCreate   # Pydantic schema for request
from models.userModel import User    # SQLAlchemy model for DB
from passlib.context import CryptContext

registerRouter = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

@registerRouter.post("/register")
def create_user(userSchema: UserCreate, db: Session = Depends(get_db)):
    # Check if user already exists
    existing_user = db.query(User).filter(User.username == userSchema.name).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    # Hash the password
    hashed_password = get_password_hash(userSchema.password)

    # Create new user object
    db_user = User(
        username=userSchema.name,
        email=userSchema.email,
        password=hashed_password
    )

    # Save to database
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user