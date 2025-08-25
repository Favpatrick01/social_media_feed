from email.mime import image
from uuid import uuid4
from fastapi import  File, Form, HTTPException,  UploadFile
from database import posts_db, users_db
from schemas.post import Post




class PostServices:

    @staticmethod
    def create_post(
        username: str = Form(...),
        title: str = Form(...),
        content: str = Form(...),
        image: UploadFile = File(None)
    ):
        # Check if the user exists
        if username not in users_db:
            raise HTTPException(status_code=404, detail="User not found")

        # Generate a unique post ID
        post_id = str(uuid4())
        image_filename = image.filename if image else None

        # Create post object
        post = Post(
            id=post_id,
            username=username,
            title=title,
            content=content,
            image_filename=image_filename
        )

        # Store in database
        posts_db[post_id] = post
        return post
    

    @staticmethod
    def get_user_posts(username: str):
        if username not in users_db:
            raise HTTPException(status_code=404, detail="User not found")

        user_posts = [post for post in posts_db.values() if post.username == username]
        return user_posts
    
    @staticmethod
    def like_post(post_id: str):
        if post_id not in posts_db:
            raise HTTPException(status_code=404, detail="Post not found")

        posts_db[post_id].likes += 1
        return posts_db[post_id]








# Initialize service
post_services = PostServices()