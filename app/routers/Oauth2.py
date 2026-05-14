from datetime import datetime,timedelta,timezone
from fastapi.security import OAuth2PasswordBearer
from fastapi import status,HTTPException,Depends
from jose import jwt,JWTError
from sqlalchemy.orm import Session
from app.models import User
from app.config import settings
from app.database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "auth/login")

def create_access_token(data : dict) -> str :
    payload = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes = settings.access_token_expire_minutes)
    payload.update({"exp" : expire , "type" : "access"})
    token = jwt.encode(payload, settings.secret_key, algorithm = settings.algorithm)
    return token

def create_refresh_token(data : dict) -> str:
    payload = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes = settings.refresh_token_expire_minutes)
    payload.update({"exp" : expire , "type" : "refresh"})
    token = jwt.encode(payload, settings.secret_key , algorithm = settings.algorithm)
    return token

def verify_access_token(token : str) -> dict:
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Could not validate credentials",
        headers = {"WWW-Authenticate" : "Bearer"}
    )
    try:
        decoded_token = jwt.decode(token,settings.secret_key,algorithms = [settings.algorithm])
        if decoded_token.get("type") != "access":
            raise credentials_exception
        username : str = decoded_token.get("sub")
        if not username:
            raise credentials_exception
        return decoded_token
    except JWTError:
        raise credentials_exception
def verify_refresh_token(token : str) -> dict:
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        details = "Could not validate credentials",
        headers = {"WWW-Authenticate" : "Bearer"}
    )
    try:
        decoded_token = jwt.decode(token, settings.secret_key, algorithms = [settings.algorithm])
        if decoded_token.get("type") != "refresh":
            raise credentials_exception
        username : str = decoded_token.get("sub")
        if not username:
            raise credentials_exception
    except JWTError:
        raise credentials_exception   
    
def get_current_user(
    token : str = Depends(oauth2_scheme),
    db : Session = Depends(get_db)
    ):
        
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        details = "Could not validate credentials",
        headers = {"WWW-AUTHENTICATE" : "Bearer"}
    )
    
    payload = verify_access_token(token,credentials_exception)
    user = db.query(User).filter(User.username == payload.get("sub")).first()
    if not user:
        raise credentials_exception
    return user

def get_current_admin(current_user : User = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(
            status_code = status.HTTP_403_FORBIDDEN,
            detail = "Access denied . Admins only",
            headers = {"WWW-Authenticate": "Bearer"}
        )
    return current_user
    
        
        
        
    
        
        
    
    
