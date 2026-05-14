from datetime import datetime 
from pydantic import BaseModel
from typing import Optional

class CampaignCreate(BaseModel):
    title : str
    description : str
    target_amount :float
    
class CampaignUpdate(BaseModel):
    title : str
    description : str
    target_amount : float
    is_active : bool

class CampaignResponse(BaseModel):
    id : int
    title : str
    description : str
    target_amount : float
    current_amount : float
    is_active : bool
    owner_id : int
    created_at : datetime
    
    class Config:
        from_attributes = True
        
    