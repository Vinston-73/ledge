from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean, func
from database.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    last_used = Column(DateTime(timezone=True), onupdate=func.now())
    is_active = Column(Boolean, default=True)