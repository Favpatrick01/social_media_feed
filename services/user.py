from fastapi import APIRouter, HTTPException, Response
from database import users_db
from schemas.user import  User


class UserServices:

    @staticmethod
    def create_user(data: User):
        if data.username in users_db:
            raise HTTPException(status_code=400, detail="User already exists")
        users_db[data.username] = data
        return data
    
user_services = UserServices()
