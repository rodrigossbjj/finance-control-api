from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime
from enum import Enum

class TransactionType(str, Enum):
    INCOME = "income"
    EXPENSE = "expense"

class TransactionBase(BaseModel):
    type: TransactionType
    amount: Decimal
    description: str | None = None
    category_id: int | None = None
    user_id: int | None = None

class TransactionCreate(TransactionBase):
    pass

class TransactionUpdate(TransactionBase):
    pass

class TransactionOut(TransactionBase):
    id: int
    date: datetime

    class Config:
        orm_mode = True
