from typing import Optional, List, Dict, Any, Union
from pydantic import BaseModel, Field

class Candidate(BaseModel):
    id: Optional[str] = Field(None, description="voter unique ID")
    name: str = Field(..., description="candidate name")
    cc: int = Field(..., description="candidate cc")
    party: str = Field(..., description="political party of the candidate")
    votes: int = Field(0, description="number of votes received by the candidate")

class CreateCandidate(BaseModel):
    name: str = Field(..., description="candidate name")
    cc: int = Field(..., description="candidate cc")
    party: str = Field(..., description="political party of the candidate")

class CandidateInfo(BaseModel):
    id: str = Field(..., description="candidate unique ID")
    name: str = Field(..., description="candidate name")
    party: str = Field(..., description="political party of the candidate")

class CandidateList(BaseModel):
    candidates: List[CandidateInfo] = Field(..., description="list of candidates")