from sqlalchemy import Integer,Boolean,Text,String,DateTime,ForeignKey,Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class Blog(Base):
    __tablename__ = "blogs"
    
    id = Column(Integer, primary_key = True, index = True)
    title = Column(String(100), nullable = False)
    content = Column(Text , nullable = True)
    cover_image = Column(String, nullable = False)
    is_published = Column(Boolean, default = False)
    author_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime(timezone=True), server_default = func.now())
    updated_at = Column(DateTime(timezone=True), server_default = func.now(), onupdate = func.now())
    
    #Relationship
    
    author = relationship("Blog", back_populates = "blogs")