from fastapi import APIRouter, HTTPException
from database import db

router = APIRouter()

@router.delete("/{user_id}", response_description="Delete user and all associated data")
async def delete_user(user_id: str):
    user = db.users.find_one({"_id": user_id})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.users.delete_one({"_id": user_id})
    db.other_collection.delete_many({"external_id": user.get("external_id")})  # Change this to your collection name
    return {"message": "User and associated data deleted successfully"}
