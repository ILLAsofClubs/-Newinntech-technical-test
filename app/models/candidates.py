from typing import Optional, List, Dict, Any, Union
from pydantic import BaseModel, Field

class Candidate(BaseModel):
    id: Optional[str] = Field(None, description="voter unique ID")
    name: str = Field(..., description="voter name")
    party: str = Field(..., description="political party of the candidate")
    votes: int = Field(0, description="number of votes received by the candidate")

class CreateCandidate(BaseModel):
    name: str = Field(..., description="voter name")
    party: str = Field(..., description="political party of the candidate")

class CandidateInfo(BaseModel):
    id: str = Field(..., description="voter unique ID")
    name: str = Field(..., description="voter name")

class CandidateList(BaseModel):
    candidates: List[CandidateInfo] = Field(..., description="list of candidates")