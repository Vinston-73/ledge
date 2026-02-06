from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, func
from backend.database.db import Base

class Setup(Base):
    __tablename__ = "setup_code"

    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    expires_at = Column(DateTime(timezone=True), index=True)
    is_used = Column(Boolean, default=False, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    nickname = Column(String, index=True)
    verification_code = Column(String, index=True)