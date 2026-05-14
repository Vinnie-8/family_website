from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base
from sqlalchemy import Column, String, DateTime, Integer, Boolean,Text,Boolean,ForeignKey

class Meeting(Base):
    __tablename__ = "meetings"
    id = Column(Integer,primary_key = True, index = True)
    title = Column(String(50), nullable = False)
    description = Column(Text, nullable = False)
    venue = Column(String(100), nullable = False)
    meeting_type = Column(String(100), default = "Regular", nullable = False)
    meeting_time = Column(DateTime(timezone=True), nullable = False)
    minutes_content = Column(Text , nullable = True)
    minutes_status = Column(String(50), default = "draft")
    is_active = Column(Boolean, default = "True")
    created_by = Column(Integer,ForeignKey("users.id"), nullable = False)
    created_at = Column(DateTime(timezone = True), server_default = func.now())
    updated_at = Column(DateTime(timezone = True), server_default = func.now(), onupdate = func.now())
    
    #Relationship 
    creator = relationship("User", back_populates = "meetings")
    attendance = relationship("Attendance", back_populates = "meeting")

