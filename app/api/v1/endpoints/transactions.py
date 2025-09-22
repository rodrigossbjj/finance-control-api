from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.transaction import Transaction
from app.schemas.transaction_schema import TransactionCreate, TransactionUpdate, TransactionOut
from app.core.auth import get_current_user
from app.models.user import User

router = APIRouter(tags=["Transactions"])

@router.get("/", response_model=list[TransactionOut])
def read_transactions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return db.query(Transaction).filter(Transaction.user_id == current_user.id).all()

@router.get("/{transaction_id}", response_model=TransactionOut)
def read_transaction(
    transaction_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    transaction = db.query(Transaction).filter(
        Transaction.id == transaction_id, Transaction.user_id == current_user.id
    ).first()
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction

@router.post("/", response_model=TransactionOut)
def create_transaction(
    transaction: TransactionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_transaction = Transaction(**transaction.dict(), user_id=current_user.id)
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

@router.put("/{transaction_id}", response_model=TransactionOut)
def update_transaction(
    transaction_id: int,
    transaction: TransactionUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_transaction = db.query(Transaction).filter(
        Transaction.id == transaction_id, Transaction.user_id == current_user.id
    ).first()
    if not db_transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    for key, value in transaction.dict(exclude_unset=True).items():
        setattr(db_transaction, key, value)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction

@router.delete("/{transaction_id}", response_model=TransactionOut)
def delete_transaction(
    transaction_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_transaction = db.query(Transaction).filter(
        Transaction.id == transaction_id, Transaction.user_id == current_user.id
    ).first()
    if not db_transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    db.delete(db_transaction)
    db.commit()
    return db_transaction
