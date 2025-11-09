import os
from dotenv import load_dotenv

load_dotenv() 

class Settings:
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "miladmin")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "milpassword")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "mil_symbols_db")
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT: int = int(os.getenv("POSTGRES_PORT", 5432))

    APP_HOST: str = os.getenv("APP_HOST", "0.0.0.0")
    APP_PORT: int = int(os.getenv("APP_PORT", 8000))

    IMAGEKIT_PRIVATE_KEY: str | None = os.getenv("IMAGEKIT_PRIVATE_KEY")
    IMAGEKIT_PUBLIC_KEY: str | None = os.getenv("IMAGEKIT_PUBLIC_KEY")
    IMAGEKIT_URL_ENDPOINT: str | None = os.getenv("IMAGEKIT_URL_ENDPOINT")

    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "info")

settings = Settings()
