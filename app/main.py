from fastapi import FastAPI, Depends
from app.database import create_db_and_tables
from app.routers.todos import router as todos_router
from app.routers.auth import router as auth_router, get_current_user
from app.models import User
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(todos_router)
app.include_router(auth_router)


@app.get("/me")
def me(current_user: User = Depends(get_current_user)):
    return {"id": current_user.id, "username": current_user.username}