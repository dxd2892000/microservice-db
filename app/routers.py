from fastapi import Depends, HTTPException, APIRouter, Form

from sqlalchemy.orm import Session

from app.databases import SessionLocal

import crud

import schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.get('users/users')
def getUser(
    name: str = Form(...),
    db: Session = Depends(get_db)
):
    return crud.get_user_by_name(db, name)
    
@router.post('users/create')
def createUser(
    name: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = schemas.UserCreate(name, password)
    return 0