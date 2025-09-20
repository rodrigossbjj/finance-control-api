# Importa o Base único do core/database
from app.core.database import Base

# Importa todas as models para que elas sejam registradas no Base
from .user import User
from .category import Category
from .transaction import Transaction
