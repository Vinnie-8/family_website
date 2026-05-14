from pydantic import BaseModel , EmailStr
from typing import Optional
from enum import Enum
from datetime import datetime

class UserRole(str,Enum):
    CHAIRMAN = "CHAIRMAN"
    SECRETARY = "SECRETARY"
    TREASURER = "TREASURER"
    MEMBER = "MEMBER"
    
class UserCreate(BaseModel):
    username : str
    full_name : str
    email : EmailStr
    phone_number : Optional[str] = None
    password : str
    role : UserRole = UserRole.MEMBER

class UserUpdate(BaseModel):
    full_name : Optional[str] = None
    email : Optional[EmailStr] = None
    phone_number : Optional[str] = None
    profile_photo : Optional[str] = None
    bio : Optional[str] = None

class UserResponse(BaseModel):
    id : int
    username : str
    full_name : str
    email : EmailStr
    phone_number :str
    profile_photo : str
    bio : str
    role : str
    is_active : bool
    created_at : datetime
    
    class Config:
        from_atttribute = True
        
class UserLogin(BaseModel):
    username : str
    password : str
class Token(BaseModel):
    acces_token : str
    refresh_token : str
    token_type : str = "bearer"
