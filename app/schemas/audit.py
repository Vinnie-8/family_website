from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AuditCreate(BaseModel):
    action : str
    entity_type : str
    entity_id : int
    description : Optional[str] =  None
    ip_address : Optional[str] = None

class AuditResponse(BaseModel):
    id : int
    action : str
    entity_type : str
    entity_id : int
    description : Optional[str] = None
    ip_address : Optional[str] = None
    user_id : int
    created_at : datetime

class Config:
    from_attributes = True
    