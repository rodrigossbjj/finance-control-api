from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate, UserRead
from app.repositories.user_repo import create_user, get_user_by_email
from app.core.database import get_db
from app.core.security import verify_password

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/register", response_model=UserRead)
def register(user: UserCreate, db: Session = Depends(get_db)):
    if get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Email já registrado")
    return create_user(db, user.email, user.password)

@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Email ou senha inválidos")
    return {"message": "Login realizado com sucesso!"}
