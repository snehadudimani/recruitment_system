from pydantic import BaseModel, EmailStr
from typing import List, Optional

class Candidate(BaseModel):
    name: str
    email: EmailStr
    resume: Optional[str] = None

class Job(BaseModel):
    title: str
    description: str
    department: str
    location: str
    employment_type: str
    required_skills: List[str]
