from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from uuid import uuid4
from pydantic import BaseModel
from typing import Optional, Dict, List


app = FastAPI()


# Models
class User(BaseModel):
    username: str
    email: str


class Post(BaseModel):
    id: str
    username: str
    title: str
    content: str
    image_filename: Optional[str] = None
    likes: int = 0


# Datebases
users_db: Dict[str, User] = {}
posts_db: Dict[str, Post] = {}



@app.post("/users/", response_model=User, status_code=201)
def create_user(data: User):
    if data.username in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    users_db[data.username] = data
    return data


@app.post("/posts/", response_model=Post, status_code=201)
def create_post(
    username: str = Form(...),
    title: str = Form(...),
    content: str = Form(...),
    image: UploadFile = File(None)
):
    if username not in users_db:
        raise HTTPException(status_code=404, detail="User not found")

    post_id = str(uuid4())
    image_filename = image.filename if image else None

    post = Post(
        id=post_id,
        username=username,
        title=title,
        content=content,
        image_filename=image_filename
    )

    posts_db[post_id] = post
    return post


@app.get("/posts/", response_model=Dict[str, Post])
def read_posts():
    return posts_db

@app.get("/users/{username}/posts", response_model=List[Post])
def get_user_posts(username: str):
    if username not in users_db:
        raise HTTPException(status_code=404, detail="User not found")

    user_posts = [post for post in posts_db.values() if post.username == username]
    return user_posts


@app.post("/posts/{post_id}/like", response_model=Post)
def like_post(post_id: str):
    if post_id not in posts_db:
        raise HTTPException(status_code=404, detail="Post not found")

    posts_db[post_id].likes += 1
    return posts_db[post_id]