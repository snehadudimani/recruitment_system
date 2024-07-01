from pydantic import BaseModel, EmailStr
from typing import List, Optional

class CandidateCreate(BaseModel):
    name: str
    email: EmailStr

class CandidateLogin(BaseModel):
    email: EmailStr

class CandidateResponse(BaseModel):
    id: str
    name: str
    email: EmailStr
    resume: Optional[str] = None

    class Config:
        orm_mode = True

class JobCreate(BaseModel):
    title: str
    description: str
    department: str
    location: str
    employment_type: str
    required_skills: List[str]

class JobResponse(BaseModel):
    id: str
    title: str
    description: str
    department: str
    location: str
    employment_type: str
    required_skills: List[str]

    class Config:
        orm_mode = True
