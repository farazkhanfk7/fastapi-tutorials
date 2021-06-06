from fastapi import APIRouter
from blog import models,schemas
from fastapi import Depends, status
from typing import List
from sqlalchemy.orm import Session
from blog.utils import get_db,get_hashed_pass

router = APIRouter(tags=['users'])

@router.get('/users', response_model=List[schemas.ShowUserDetail])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users


@router.post('/user', status_code = status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    user_detail = request.dict()
    password = user_detail.get('password')
    user_detail['password'] = get_hashed_pass(password)
    new_user = models.User(**user_detail)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"detail":"user created succesfully"}