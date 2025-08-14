 from fastapi import FastAPI, File, UploadFile, Form, HTTPException

from uuid import UUID, uuid4
from pydantic import BaseModel
from typing import Optional
from typing import Annotated


app = FastAPI()


class User(BaseModel):
     username: str 
     email: str
     password : str
    
   

class Post(BaseModel):
    id: int 
    username: str
    title: str
    content: str
    image_filename: Optional[str]= None
    likes: int = 0



posts_db = {}


@app.post("/users/", response_model=User, status_code=201)
def create_user(data: User):
       if data.username in posts_db:
           raise HTTPException(status_code=400, detail="User already exists")
       posts_db[data.username] = data
       return data



@app.post("/posts/", response_model=Post, status_code=201)
def create_post(data: Post = Form()):
        posts_db[data.content] = data
        return data


@app.get("/posts/", response_model=dict[str, Post])
def read_post():
       return posts_db



    

@app.get("/users/{username}/posts", response_model=dict[str, Post])
def get_post_by_username(username : str):
        if username not in posts_db:
            raise HTTPException(status_code=404, detail="Post not found")   
        return posts_db


@app.put("/posts/{post_id}/like")
def like_post(post_id: int):
       post_id == id
       if post_id not in posts_db:
           raise HTTPException(status_code=404, detail="Post not found")
   
       post = posts_db[post_id]
       if id in post.likes:
           raise HTTPException(status_code=400, detail="User already liked the post")
   
       post.likes.append(id)
       




 


