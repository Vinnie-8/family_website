from pydantic import BaseModel
from typing import Optional
from enum import Enum
from datetime import datetime


class MinutesStatus(str,Enum):
    DRAFT  = "draft"
    PUBLISHED = "published"
    LOCKED = "locked"
    
class MeetingCreate(BaseModel):
    title : str
    description : Optional[str] = None
    venue : str
    meeting_time : datetime
    meeting_type : Optional[str] = "regular"
    
class MeetingUpdate(BaseModel):
    title : Optional[str] = None
    description : Optional[str] = None
    venue : Optional[str] = None
    meeting_time : Optional[datetime] = None
    minutes_content : Optional[str] = None
    minutes_status : Optional[MinutesStatus] = None
    is_active : Optional[bool] = None
    

class MeetingResponse(BaseModel):
    id : int
    title : str
    description : Optional[str]
    venue : str
    meeting_time : datetime
    meeting_type : str
    minutes_content :Optional[str]
    minutes_status : str
    is_active : bool
    created_by : int
    created_at : datetime
    class Config:
        from_attributes = True
        
        
    
    

    

    