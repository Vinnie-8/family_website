from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class BlogCreate(BaseModel):
    title : str
    content : str
    
class BlogUpdate(BaseModel):
    title : Optional[str] = None
    content : Optional[str] = None
    
class BlogResponse(BaseModel):
    id : int
    title : str
    content : str
    author_id : int
    created_at : int
    updated_at : Optional[datetime]
    class Config:
        from_attributes = True
     
    
