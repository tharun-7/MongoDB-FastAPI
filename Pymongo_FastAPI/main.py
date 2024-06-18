from fastapi import FastAPI
from routes import user, auth, link, join, delete
from database import client

app = FastAPI()

# Include routers for different functionalities
app.include_router(user.router, prefix="/user", tags=["User"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(link.router, prefix="/link", tags=["Link"])
app.include_router(join.router, prefix="/join", tags=["Join"])
app.include_router(delete.router, prefix="/delete", tags=["Delete"])

# Connect to the database when the app starts
@app.on_event("startup")
def startup_db_client():
    client

# Close the database connection when the app shuts down
@app.on_event("shutdown")
def shutdown_db_client():
    client.close()
