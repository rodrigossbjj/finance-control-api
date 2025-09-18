from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_JWT: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
