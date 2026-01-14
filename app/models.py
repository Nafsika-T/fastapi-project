
from sqlmodel import SQLModel, Field
from typing import Optional

class Todo(SQLModel, table = True):
    id: int | None = Field(default= None, primary_key= True)
    title: str
    description: str | None = None
    completed: bool = False
    owner_id: int = Field(foreign_key= "user.id")

class TodoCreate(SQLModel):
    title: str
    description: str | None = None
    completed: bool = False

class TodoUpdate(SQLModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None

class User(SQLModel, table= True):
    id: int | None = Field(default= None, primary_key= True)
    username: str = Field(index= True, unique= True)
    hashed_password: str

class UserCreate(SQLModel):
    username: str
    password: str

class UserRead(SQLModel):
    id: int
    username: str

class UserLogin(SQLModel):
    username: str
    password: str

class TodoRead(SQLModel):
    id: int
    title: str
    description: str | None
    completed: bool