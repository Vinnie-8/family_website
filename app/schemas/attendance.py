from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class AttendanceCreate(BaseModel):
    meeting_id : int
    user_id : int
    
class AttendanceResponse(BaseModel):
    id : int
    meeting_id : int
    user_id : int
    created_at : datetime
    
    class Config:
        from_attribute = True