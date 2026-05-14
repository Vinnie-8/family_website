from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy.sql import func
from sqlalchemy import String, Integer, Float , Text, Column, DateTime,ForeignKey , Boolean

class Campaign(Base):
    __tablename__ = "campaigns"
    id = Column(Integer,primary_key = True , index = True)
    title = Column(String(150), nullable = False)
    description = Column(Text, nullable = False)
    target_amount = Column(Float,nullable = False)
    current_amount = Column(Float, default = 0)
    is_active = Column(Boolean, default = True)
    owner_id = Column(Integer , ForeignKey("users.id"))
    created_at = Column(DateTime(timezone=True) , server_default = func.now())
    
    #Relationships
    owner = relationship("User" , back_populates = "campaigns")
    pledges = relationship("Pledge" , back_populates = "campaign")
    payments = relationship("Payment", back_populates = "campaign")
    