from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from database import db
from utils.security import verify_password
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str

@router.post("/login", response_description="Login user")
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    user = db.users.find_one({"email": form_data.username})
    if not user or not verify_password(form_data.password, user['password']):
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return {"message": "Login successful"}
