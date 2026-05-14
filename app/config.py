from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    DATABASE_URL : str = ""
    SECRET_KEY : str = ""
    ALGORITHM :str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES : int = 30
    REFRESH_TOKEN_EXPIRE_DAYS : int = 30
    
    # M-Pesa
    MPESA_CONSUMER_KEY: Optional[str] = None
    MPESA_CONSUMER_SECRET: Optional[str] = None
    MPESA_SHORTCODE: Optional[str] = None
    MPESA_PASSKEY: Optional[str] = None
    MPESA_CALLBACK_URL: Optional[str] = None

    # Email
    MAIL_USERNAME: Optional[str] = None
    MAIL_PASSWORD: Optional[str] = None
    MAIL_FROM: Optional[str] = None
    MAIL_FROM_NAME: str = "Family Website"
    MAIL_SERVER: str = "smtp.gmail.com"
    MAIL_PORT: int = 587

    # Africa's Talking SMS
    AT_USERNAME: Optional[str] = None
    AT_API_KEY: Optional[str] = None
    AT_SENDER_ID: Optional[str] = None

    # App
    APP_NAME: str = "Family Website"
    ENVIRONMENT: str = "development"

    class Config:
        env_file = ".env"


settings = Settings()