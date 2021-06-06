from pydantic import BaseModel
from typing import Optional

class Blog(BaseModel):
    title : str
    body : str

class ShowBlog(Blog):
    class Config:
        orm_mode = True

class User(BaseModel):
    username : str
    email : str
    password : str 

class ShowUser(BaseModel):
    username : str
    email : str
    
    class Config:
        orm_mode = True
