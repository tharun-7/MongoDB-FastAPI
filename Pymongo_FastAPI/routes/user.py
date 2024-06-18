from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel, EmailStr
from models import UserModel
from database import db
from utils.security import get_password_hash

router = APIRouter()

class UserRegisterSchema(BaseModel):
    username: str
    email: EmailStr
    password: str

@router.post("/register", response_description="Register a new user")
async def register_user(user: UserRegisterSchema):
    if db.users.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = get_password_hash(user.password)
    user.password = hashed_password
    new_user = UserModel(**user.dict())
    db.users.insert_one(new_user.dict(by_alias=True))
    return {"message": "User registered successfully"}
