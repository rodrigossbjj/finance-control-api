from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import get_password_hash

def create_user(db: Session, email: str, password: str) -> User:
    user = User(email=email, hashed_password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()
