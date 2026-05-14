from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base
from sqlalchemy import Column,String ,Float, ForeignKey, DateTime,Integer

class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key = True,index = True)
    amount = Column(Float,nullable = False)
    payment_method = Column(String(100) , nullable = False)
    status = Column(String , default = "completed")
    transaction_code = Column(String(100), unique = True)
    user_id = Column(Integer,ForeignKey("users.id"))
    campaign_id = Column(Integer, ForeignKey("campaigns.id"))
    pledge_id = Column(Integer, ForeignKey("pledges.id"))
    created_at = Column(DateTime(timezone=True),server_default = func.now())
    
    #Relationships
    
    user = relationship("User", back_populates = "payments")
    campaign = relationship("Campaign", back_populates = "payments")
    pledge = relationship("Pledge", back_populates = "payments")