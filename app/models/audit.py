from sqlalchemy import Column,String,Integer,Text,DateTime,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Audit(Base):
    __tablename__ = "audits"
    
    id = Column(Integer, primary_key = True, index = True)
    action = Column(String(100), nullable=False)
    description = Column(Text , nullable = True)
    ip_address = Column(String , nullable = True)
    entity_type = Column(String(50),  nullable=True)  # "user" "payment" "campaign"
    entity_id   = Column(Integer,     nullable=True)  # id of affected record
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime(timezone=True), server_default = func.now())
    
    #Relationship
    
    user = relationship("User", back_populates = "audits") 