

from fastapi import HTTPException,status,Depends
from fastapi.security import OAuth2PasswordBearer
import jwt
from sqlalchemy.orm import Session
from auth.security import ALGORITHM, SECRET_KEY
from models.userModel import User
from database.db import get_db
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def get_current_user(token:str=Depends(oauth2_scheme),
db:Session=Depends(get_db)):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        name:str = payload.get("sub")
        if name is None:
            raise credentials_exception
    except jwt.InvalidTokenError:
        raise credentials_exception
    user = db.query(User).filter(User.name==name).first()
    if user is None:
        raise credentials_exception
    return user

