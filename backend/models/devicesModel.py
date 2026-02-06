import datetime
from click import DateTime
from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, String, func
from backend.database.db import Base
class Device(Base):
    __tablename__ = "devices"
    
    # id = Column(Integer, primary_key=True, index=True)
    # user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    # username = Column(String, index=True)
    # device_name = Column(String, index=True)
    # email = Column(String, index=True)
    device_token = Column(String, index=True)
    # created_at = Column(DateTime(timezone=True), server_default=func.now())
    # last_used = Column(DateTime(timezone=True), onupdate=func.now())
    # is_active = Column(Boolean, default=True)
