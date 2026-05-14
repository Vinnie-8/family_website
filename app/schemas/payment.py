from enum import Enum
from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class PaymentMethod(str,Enum):
    MPESA = "MPESA"
    CASH = "CASH"
    
class PaymentStatus(str,Enum):
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    REJECTED = "REJECTED"
    
class PaymentCreate(BaseModel):
    pledge_id : int
    method : PaymentMethod
    amount : float
    transaction_ref : Optional[str] = None
    
class PaymentUpdate(BaseModel):
    status : Optional[PaymentStatus] = None

class PaymentResponse(BaseModel):
    id : int
    amount : float
    method : PaymentMethod
    status : PaymentStatus
    pledge_id : int
    campaign_id : int
    user_id : int
    transaction_ref : Optional[str] = None
    created_at : datetime
    
    class Config:
        from_attributes = True
        
        
        