import models, schemas
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from utils import get_db
from database import engine
import uvicorn

models.Base.metadata.create_all(engine)

app = FastAPI()

@app.get('/{name}')
def index(name):
    return {"name":name}


@app.post('/blog')
def new_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title,body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return {"data_recieved": new_blog}


if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=9000)