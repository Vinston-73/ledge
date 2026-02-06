


from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from backend.database.db import Base
from backend.models.devicesModel import Device
from backend.models.userModel import user



class EventDaily(Base):
    __tablename__ = "event_daily"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer,ForeignKey(user.id,ondelete="CASCADE"),nullable=False)
    device_id = Column(Integer, ForeignKey(Device.id, ondelete="CASCADE"), nullable=False)
    event_type = Column(String, index=True)
    date = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    event_count = Column(Integer, index=True)