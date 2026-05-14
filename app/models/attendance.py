from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy import Column, Integer,String,ForeignKey,Boolean,DateTime

class Attendance(Base):
    __tablename__ = "attendance"
    
    id = Column(Integer, primary_key = True , index = True)
    meeting_id = Column(Integer, ForeignKey("meetings.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    present = Column(Boolean, default = True)
    created_at = Column(DateTime(timezone = True), server_default = func.now())
    
    user = relationship("User", back_populates = "attendance")
    meeting = relationship("Meeting", back_populates = "attendance")
    