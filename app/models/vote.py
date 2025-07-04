from typing import Optional, List, Dict, Any, Union
from pydantic import BaseModel, Field

class Vote(BaseModel):
    id: Optional[str] = Field(None, description="voter unique ID")
    voter_id: str = Field(..., description="ID of the voter who cast the vote")
    candidate_id: str = Field(..., description="ID of the candidate who received the vote")