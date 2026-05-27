from passlib.context import CryptContext
from app.database import get_db
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.config import settings
from app import models
from fastapi import Depends,HTTPException,status,APIRouter,Body
from routers.auth import create_access_token, create_refresh_token,verify_refresh_token
from app import schemas


pwd_context = CryptContext(schemes = ["bcrypt"], deprecated = "auto")

def hash_password(password : str) -> str:
    return pwd_context.hash(password)

def verify_password (plain_password : str , hashed_password:str) -> bool:
    return pwd_context.verify(plain_password,hashed_password)

router = APIRouter(prefix = "/auth", tags = ["authentication"])

@router.post("/register" , response_model = schemas.UserResponse)
def register(user:schemas.UserCreate, db : Session = Depends(get_db))-> models.User:
    existing_user = db.query(models.User).filter(models.User.username == user.username).first()
    if existing_user:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            details = "Username already registered"
        )
    existing_email = db.query(models.User).filter(models.User.email == user.email).first()
    if existing_email:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            details = "Email already registered"
        )

    hashed_password = hash_password(user.password)
    new_user = models.User(username = user.username , email = user.email, hashed_password = hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/login" , response_model = schemas.Token)
def login(form_data : OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db)) -> models.User:
    credentials_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        details = "Invalid email or password",
        headers = {"WWW-Authenticate" : "Bearer"}
    )
    user = db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user or verify_password(form_data.password, user.hashed_password):
        raise credentials_exception
    access_token = create_access_token(data = {"sub" : user.username})
    refresh_token = create_refresh_token(data = {"sub" : user.username})
    return {"access_token" : access_token , "refresh_token" : refresh_token , "token_type" : "bearer"}

@router.post("/refresh", response_model = schemas.Token)
def refresh(token : str = Body(...), db : Session = Depends(get_db)) -> dict:
    payload = verify_refresh_token(token)
    username : str | None = payload.get("sub")
    if not username :
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            details = "Invelid credentials",
            headers = {"WWW-Authenticate" : "Bearer"}
        )
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user :
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            details = "Invelid credentials",
            headers = {"WWW-Authenticate" : "Bearer"})
    
    new_access_token = create_access_token(data = {"sub" : user.username})
    new_refresh_token = create_refresh_token(data = {"sub" : user.username})
    return {
        "access_token" : new_access_token,
        "refresh_token" : new_refresh_token,
        "token_type" : "bearer"
    }
@router.post("/logout")
def logout():
    return {"message": "Logged out successfully"}