from fastapi import FastAPI
from app.database import client
from app.routers import candidates, admin, jobs

app = FastAPI()

app.include_router(candidates.router, prefix="/candidates", tags=["candidates"])
app.include_router(admin.router, prefix="/admin", tags=["admin"])
app.include_router(jobs.router, prefix="/jobs", tags=["jobs"])

@app.get("/")
async def read_root():
    return {"message": "Welcome to the Recruitment System"}

@app.on_event("startup")
async def startup_db_client():
    print("Connecting to MongoDB")
    client.admin.command('ping')

@app.on_event("shutdown")
async def shutdown_db_client():
    print("Closing MongoDB connection")
    client.close()
