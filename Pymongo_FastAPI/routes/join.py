from fastapi import APIRouter
from database import db

router = APIRouter()

@router.get("/", response_description="Join data from multiple collections")
async def join_data():
    pipeline = [
        {
            "$lookup": {
                "from": "other_collection",  # Change this to your collection name
                "localField": "external_id",
                "foreignField": "external_id",
                "as": "joined_data"
            }
        }
    ]
    result = list(db.users.aggregate(pipeline))
    return result
