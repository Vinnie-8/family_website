from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class PledgeCreate(BaseModel):
    campaign_id : int
    amount : float
class PledgeUpdate(BaseModel):
    amount : Optional[int] = None
class PledgeResponse(BaseModel):
    id : int 
    amount : float
    campaign_id : float
    user_id : int
    created_at : datetime
    
    class Config:
        from_attributes = True
        