from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.database import get_session
from app.models import User, UserCreate, UserRead
from app.auth import hash_password, verify_password, create_access_token, get_current_user

from fastapi.security import OAuth2PasswordRequestForm

router= APIRouter(prefix= "/auth", tags= ["auth"])


@router.post("/register", response_model= UserRead)
def register(user_data: UserCreate, session: Session = Depends(get_session)):
    
    existing= session.exec(select(User).where( User.username == user_data.username)).first()

    if existing:
        raise HTTPException(status_code=409, detail="Username already exists")    
    user= User(
        username= user_data.username,
        hashed_password= hash_password(user_data.password) 
    )

    session.add(user)
    session.commit()
    session.refresh(user)

    return user

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    
    user = session.exec(select(User).where(User.username == form_data.username)).first()

    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "bearer"}

