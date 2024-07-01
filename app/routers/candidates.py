from fastapi import APIRouter, HTTPException
from app.schemas import CandidateCreate, CandidateLogin, CandidateResponse
from app.crud import create_candidate, get_candidate, get_all_candidates
from typing import List

router = APIRouter()

@router.post("/signup", response_model=CandidateResponse)
async def signup(candidate: CandidateCreate):
    existing_candidate = await get_candidate(candidate.email)
    if existing_candidate:
        raise HTTPException(status_code=400, detail="Email already registered")
    candidate_id = await create_candidate(candidate)
    return CandidateResponse(id=candidate_id, **candidate.dict())

@router.post("/login", response_model=CandidateResponse)
async def login(candidate: CandidateLogin):
    existing_candidate = await get_candidate(candidate.email)
    if not existing_candidate:
        raise HTTPException(status_code=404, detail="Candidate not found")
    return CandidateResponse(id=str(existing_candidate.id), **existing_candidate.dict())

@router.get("/candidates", response_model=List[CandidateResponse])
async def get_candidates():
    candidates = await get_all_candidates()
    return [CandidateResponse(id=str(candidate.id), **candidate.dict()) for candidate in candidates]
