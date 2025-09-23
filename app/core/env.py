from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_JWT: str

    class Config:
        env_file = os.getenv("ENV_FILE", ".env")
        env_file_encoding = "utf-8"

settings = Settings()
