from sqlalchemy import String,Integer,Enum,Float,Boolean,DateTime,Text,Column
from app.database import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import enum

class UserRole(str, enum.Enum):
    CHAIRMAN = "chairman"
    TREASURER  = "treasurer"
    SECRETARY = "secretary"
    MEMBER = "member"
    
class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key = True, index = True)
    username = Column(String(50),unique=True,index=True,nullable = False)
    full_name = Column(String(100),nullable = False)
    email = Column(String(50),unique = True,index = True, nullable = False)
    phone_number = Column(String(50), nullable = True)
    hashed_password = Column(String(200),nullable=False)
    role = Column(Enum(UserRole), default = UserRole.MEMBER , nullable = False)
    profile_photo = Column(String, nullable = True)
    bio = Column(Text, nullable = True)
    is_admin = Column(Boolean , default = False)
    is_active = Column(Boolean, default = True)
    is_public = Column(Boolean, default = False)
    created_at = Column(DateTime(timezone = True), server_default =func.now())
    updated_at = Column(DateTime(timezone = True), onupdate = func.now())
    
    #Relationships
    campaigns = relationship("Campaign" , back_populates = "owner")
    payments = relationship("Payment", back_populates = "user")
    blogs = relationship("Blog" , back_populates = "author")
    pledges = relationship("Pledge", back_populates = "user")
    audits = relationship("Audit", back_populates = "user")
    attendance = relationship("Attendance" , back_populates = "user")
    meetings = relationship("Meeting", back_populates = "creator")
    
    