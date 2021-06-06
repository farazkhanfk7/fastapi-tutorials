from pydantic import BaseModel
from typing import Optional,List

class Blog(BaseModel):
    title : str
    body : str

class ShowBlogOnly(Blog):
    class Config:
        orm_mode = True

class ShowUserDetail(BaseModel):
    username : str
    email : str
    blogs : List[ShowBlogOnly]
    
    class Config:
        orm_mode = True

class ShowUserOnly(BaseModel):
    username : str
    email : str
    
    class Config:
        orm_mode = True

class ShowBlogDetail(Blog):
    author : ShowUserOnly
    class Config:
        orm_mode = True

class User(BaseModel):
    username : str
    email : str
    password : str 
