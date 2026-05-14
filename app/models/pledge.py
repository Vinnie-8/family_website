from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy import Integer, Column , String ,Float, DateTime,ForeignKey

class Pledge(Base):
    __tablename__ = "pledges"
    id = Column(Integer, primary_key = True , index = True)
    amount = Column(Float, nullable = False)
    status = Column(String(50), default = "pending")
    user_id = Column(Integer, ForeignKey("users.id"))
    campaign_id = Column(Integer , ForeignKey("campaigns.id"))
    created_at = Column(DateTime(timezone=True), server_default = func.now())
    
    #Relationship 
    user = relationship("User" , back_populates = "pledges")
    campaign = relationship("Campaign", back_populates = "pledges")
    payments = relationship("Payment", back_populates = "pledge")
    
    