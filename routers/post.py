from typing import Dict, List
from fastapi import APIRouter, File, Form, HTTPException, Response, UploadFile
from schemas.post import Post
from services.post import post_services
from database import posts_db



post_router = APIRouter()



@post_router.post("", response_model=Post, status_code=201)
def create_post(
    username: str = Form(...),
    title: str = Form(...),
    content: str = Form(...),
    image: UploadFile = File(None)
):
    return post_services.create_post(username, title, content, image)



@post_router.get("", response_model=Dict[str, Post])
def read_posts():
    return posts_db



@post_router.get("{username}", response_model=List[Post])
def get_user_posts(username: str):
    post = post_services.get_user_posts(username)
    return post


@post_router.post("{post_id}", response_model=Post)
def like_post(post_id: str):
    like = post_services.like_post(post_id)
    return like