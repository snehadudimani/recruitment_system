from app.database import candidates_collection, jobs_collection
from app.models import Candidate, Job
from bson import ObjectId
from typing import List, Optional

# Candidates CRUD
async def create_candidate(candidate: Candidate):
    candidate_dict = candidate.dict()
    result = await candidates_collection.insert_one(candidate_dict)
    return str(result.inserted_id)

async def get_candidate(email: str) -> Optional[Candidate]:
    candidate = await candidates_collection.find_one({"email": email})
    if candidate:
        return Candidate(**candidate)
    return None

async def get_all_candidates() -> List[Candidate]:
    candidates = []
    async for candidate in candidates_collection.find():
        candidates.append(Candidate(**candidate))
    return candidates

# Jobs CRUD
async def create_job(job: Job):
    job_dict = job.dict()
    result = await jobs_collection.insert_one(job_dict)
    return str(result.inserted_id)

async def get_all_jobs() -> List[Job]:
    jobs = []
    async for job in jobs_collection.find():
        jobs.append(Job(**job))
    return jobs

async def apply_for_job(candidate_id: str, job_id: str):
    result = await candidates_collection.update_one(
        {"_id": ObjectId(candidate_id)},
        {"$addToSet": {"applied_jobs": job_id}}
    )
    return result.modified_count > 0
