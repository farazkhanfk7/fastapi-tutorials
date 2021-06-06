from blog.database import SessionLocal
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_hashed_pass(password: str):
    return pwd_context.hash(password)

def verify_password(plain_pass: str,hashed_pass: str):
    return pwd_context.verify(plain_pass, hashed_pass) 