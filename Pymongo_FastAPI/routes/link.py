from fastapi import APIRouter, HTTPException, Body
from pydantic import BaseModel
from database import db

router = APIRouter()

class LinkIDSchema(BaseModel):
    user_id: str
    external_id: str

@router.post("/", response_description="Link an ID to a user's account")
async def link_id(data: LinkIDSchema):
    user = db.users.find_one({"_id": data.user_id})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.users.update_one({"_id": data.user_id}, {"$set": {"external_id": data.external_id}})
    return {"message": "ID linked successfully"}
