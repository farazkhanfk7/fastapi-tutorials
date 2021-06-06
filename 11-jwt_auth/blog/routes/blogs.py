from fastapi import APIRouter
from blog import models,schemas
from fastapi import Depends, status, Response, HTTPException
from typing import List
from sqlalchemy.orm import Session
from blog.utils import get_db

router = APIRouter(tags=['blogs'])


@router.get('/blogs/', response_model=List[schemas.ShowBlogDetail])
def blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@router.post('/blog', status_code=status.HTTP_201_CREATED)
def new_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title,body=request.body,author_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return {"data_recieved": new_blog}


@router.get('/blog/{id_}', status_code=200, response_model=schemas.ShowBlogDetail)
def blogs(id_, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id_).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"data":f"blog with {id_} not found"}
        # or raise exceptions
        raise HTTPException(status_code=404,detail=f"blog with {id_} not found")
    return blog


@router.delete('/blog/{id_}')
def delete_blog(id_, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id_)
    if not blog.first():
        raise HTTPException(status_code=404,detail=f"blog with {id_} not found")
    else:
        blog.delete(synchronize_session=False)
        db.commit()
        return {"data":f"blog with {id_} deleted succesfully"}


@router.put('/blog/{id_}')
def update_blog(id_,request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id_)
    if not blog.first():
        raise HTTPException(status_code=404,detail=f"blog with {id_} not found")
    x = request.dict()
    blog.update(x)
    db.commit()
    return {"data":f"blog with {id_} updated succesfully"}