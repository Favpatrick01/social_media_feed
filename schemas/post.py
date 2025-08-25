from pydantic import BaseModel
from typing import Optional


class Post(BaseModel):
    id: str
    username: str
    title: str
    content: str
    image_filename: Optional[str] = None
    likes: int = 0