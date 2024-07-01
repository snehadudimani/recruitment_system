from fastapi import APIRouter
from app.schemas import CandidateResponse
from app.crud import get_all_candidates
from typing import List

router = APIRouter()

@router.get("/candidates", response_model=List[CandidateResponse])
async def get_candidates():
    candidates = await get_all_candidates()
    return [CandidateResponse(id=str(candidate.id), **candidate.dict()) for candidate in candidates]
