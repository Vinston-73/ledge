from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from database.db import Base

class Events(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    device_id = Column(Integer, ForeignKey("devices.id", ondelete="CASCADE"), nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    source = Column(String, index=True)
    event_type = Column(String, index=True)
    payload = Column(String, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())