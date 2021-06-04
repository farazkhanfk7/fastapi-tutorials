from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI()

@app.get('/{name}')
def index(name):
    return {"name":name}


class Blog(BaseModel):
    title : str
    body : str
    published_at : Optional[bool]


@app.post('/blog')
def new_blog(request: Blog):
    return {"data_recieved": request}


if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=9000)