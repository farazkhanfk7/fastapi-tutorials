from blog import models, schemas
from fastapi import FastAPI, Depends, status, Response, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from sqlalchemy.orm import Session
from blog.utils import get_db,get_hashed_pass
from blog.database import engine
from blog.routes import users,blogs,auth
import uvicorn

models.Base.metadata.create_all(engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(blogs.router)
app.include_router(auth.router)



@app.get('/')
def index():
    return {"data":"not yet"}

if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1",port=9000)