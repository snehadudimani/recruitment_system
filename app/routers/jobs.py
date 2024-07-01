from fastapi import APIRouter, HTTPException
from app.schemas import JobCreate, JobResponse
from app.crud import create_job, get_all_jobs, apply_for_job
from typing import List
from bson import ObjectId  # Add this import

router = APIRouter()

@router.post("/", response_model=JobResponse)
async def create_job(job: JobCreate):
    job_id = await create_job(job)
    return JobResponse(id=job_id, **job.dict())

@router.get("/", response_model=List[JobResponse])
async def get_jobs():
    jobs = await get_all_jobs()
    return [JobResponse(id=str(job.id), **job.dict()) for job in jobs]

@router.post("/apply/{candidate_id}/{job_id}")
async def apply(candidate_id: str, job_id: str):
    if not ObjectId.is_valid(candidate_id) or not ObjectId.is_valid(job_id):
        raise HTTPException(status_code=400, detail="Invalid candidate or job ID")
    success = await apply_for_job(candidate_id, job_id)
    if not success:
        raise HTTPException(status_code=404, detail="Candidate or Job not found")
    return {"message": "Application successful"}
