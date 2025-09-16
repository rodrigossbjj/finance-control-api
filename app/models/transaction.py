from enum import Enum as PyEnum
from decimal import Decimal
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Text, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy import Enum as SqEnum
from app.core.database import Base


class TransactionType(PyEnum):
    INCOME = "income"
    EXPENSE = "expense"


class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(SqEnum(TransactionType, name="transaction_type"), nullable=False, index=True)
    amount = Column(Numeric(12, 2), nullable=False)  # usar Decimal ao trabalhar com valor
    description = Column(Text, nullable=True)

    # data da transação (timezone-aware)
    date = Column(DateTime(timezone=True), server_default=func.now(), nullable=False, index=True)

    # relacionamentos
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True, index=True)
    category = relationship("Category", back_populates="transactions")

    user_id = Column(Integer, ForeignKey("users.id"), nullable=True, index=True)
    user = relationship("User", back_populates="transactions")

    def __repr__(self):
        return f"<Transaction id={self.id} type={self.type} amount={self.amount}>"
