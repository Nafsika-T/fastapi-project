from fastapi import APIRouter, Depends, HTTPException, Response
from sqlmodel import Session, select
from app.database import get_session
from app.models import Todo, TodoCreate, TodoUpdate, User, TodoRead
from app.auth import get_current_user


router= APIRouter(prefix= "/todos", tags= ["todos"])

@router.get("", response_model= list[TodoRead])
def read_todos(session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    todos = session.exec(select(Todo).where(Todo.owner_id == current_user.id)).all()
    return todos

@router.get("/{todo_id}", response_model= TodoRead)
def read_todo(todo_id: int, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    todo = session.exec(select(Todo).where(Todo.id == todo_id, Todo.owner_id == current_user.id)).first()
    if not todo:
        raise HTTPException(status_code= 404, detail= "Todo not found")
    return todo


@router.delete("/{todo_id}")
def delete_todo(todo_id: int, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    todo = session.exec(select(Todo).where(Todo.id == todo_id, Todo.owner_id == current_user.id)).first()
    if not todo:
        raise HTTPException(status_code= 404, detail= "Todo not found")
    
    session.delete(todo)
    session.commit()

    return Response(status_code=204)

@router.post("", response_model= TodoRead, status_code= 201)
def create_todo(todo: TodoCreate, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    new_todo = Todo(**todo.model_dump(), owner_id= current_user.id)
    session.add(new_todo)
    session.commit()
    session.refresh(new_todo)
    return new_todo


@router.put("/{todo_id}", response_model= TodoRead)
def update_todo(todo_id: int, todo_data: TodoCreate, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    
    todo = session.exec(select(Todo).where(Todo.id == todo_id, Todo.owner_id == current_user.id)).first()

    if not todo:
        raise HTTPException(status_code= 404, detail= "Todo not found" )

    todo.title = todo_data.title
    todo.description = todo_data.description
    todo.completed = todo_data.completed

    session.add(todo)
    session.commit()

    return todo

@router.patch("/{todo_id}", response_model= TodoRead)
def patch_todo(todo_id: int, todo_data: TodoUpdate, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):

    todo = session.exec(select(Todo).where(Todo.id == todo_id, Todo.owner_id == current_user.id)).first()

    if not todo:
        raise HTTPException(status_code= 404, detail= "Todo not found")
    
    update_data = todo_data.model_dump(exclude_unset= True)

    for key, value in update_data.items():
        setattr(todo, key, value)

    session.add(todo)

    session.commit()

    return todo