from typing import Dict
from schemas.user import User
from schemas.post import Post

# Datebases
users_db: Dict[str, User] = {}
posts_db: Dict[str, Post] = {}