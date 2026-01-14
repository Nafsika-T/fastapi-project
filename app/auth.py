from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlmodel import Session, select
from app.database import get_session
from app.models import User
from app.config import SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES

ALGORITHM = "HS256"

oauth2_scheme= OAuth2PasswordBearer(tokenUrl= "/auth/login")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_minutes: int = ACCESS_TOKEN_EXPIRE_MINUTES) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_minutes)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm= ALGORITHM)

def get_current_user(token: str= Depends(oauth2_scheme), session: Session = Depends(get_session)):
    try:
        payload= jwt.decode(token, SECRET_KEY, algorithms= [ALGORITHM])
        username= payload.get("sub")
        if username is None:
            raise HTTPException(status_code= 401, detail= "Invalid token")
    except JWTError:
        raise HTTPException(status_code= 401, detail= "Invalid token")
    
    user= session.exec(select(User).where(User.username == username)).first()
    
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user



