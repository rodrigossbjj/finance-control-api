from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from app.core.env import settings

DATABASE_URL = settings.DATABASE_URL

# Engine = conexão com o PostgreSQL
engine = create_engine(DATABASE_URL)

# Session = "ponte" para enviar queries
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = usada pelas models
Base = declarative_base()

# Dependência para usar em endpoints
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
