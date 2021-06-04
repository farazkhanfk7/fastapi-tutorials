import models, schemas
from fastapi import FastAPI, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from utils import get_db
from database import engine
import uvicorn

models.Base.metadata.create_all(engine)

app = FastAPI()

@app.get('/')
def index():
    return {"data":"not yet"}


@app.post('/blog', status_code=status.HTTP_201_CREATED)
def new_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return {"data_recieved": new_blog}


@app.get('/blogs/')
def blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get('/blog/{id_}', status_code=200)
def blogs(id_, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id_).first()
    if not blog:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"data":f"blog with {id_} not found"}
        # or raise exceptions
        raise HTTPException(status_code=404,detail=f"blog with {id_} not found")
    return blog


@app.delete('/blog/{id_}')
def delete_blog(id_, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id_)
    if not blog.first():
        raise HTTPException(status_code=404,detail=f"blog with {id_} not found")
    else:
        blog.delete(synchronize_session=False)
        db.commit()
        return {"data":f"blog with {id_} deleted succesfully"}


@app.put('/blog/{id_}')
def update_blog(id_,request: schemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id_)
    if not blog.first():
        raise HTTPException(status_code=404,detail=f"blog with {id_} not found")
    x = request.dict()
    blog.update(x)
    db.commit()
    return {"data":f"blog with {id_} updated succesfully"}

if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=9000)