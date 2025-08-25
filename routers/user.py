from fastapi import APIRouter, HTTPException, Response
from schemas.user import User
from services.user import user_services



user_router = APIRouter()



@user_router.post("", response_model=User, status_code=201)
def create_user(data: User):
    user = user_services.create_user(data)
    if not user:
        raise HTTPException(status_code=404, detail="User not found") 
    return user