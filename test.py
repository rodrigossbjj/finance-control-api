from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
plain = "123456"
stored_hash = "$2b$12$9kSaHabDy4sXArVhOnSaf.l.gb2hS.d7zI9J7KGec/3ynCNyv51X6"  # do seu DB

print("verify:", pwd_context.verify(plain, stored_hash))
