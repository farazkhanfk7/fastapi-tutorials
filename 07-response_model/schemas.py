from pydantic import BaseModel
from typing import Optional

class Blog(BaseModel):
    title : str
    body : str

class ShowBlog(Blog):
    class Config:
        orm_mode = True