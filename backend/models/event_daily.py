from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from database.db import Base
from models.devicesModel import Device
from models.userModel import User
class EventDaily(Base):
    __tablename__ = "event_daily"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer,ForeignKey(User.id,ondelete="CASCADE"),nullable=False)
    device_id = Column(Integer, ForeignKey(Device.id, ondelete="CASCADE"), nullable=False)
    event_type = Column(String, index=True)
    date = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    event_count = Column(Integer, index=True)