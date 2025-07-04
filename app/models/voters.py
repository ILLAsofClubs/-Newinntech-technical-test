from typing import Optional, List, Dict, Any, Union
from pydantic import BaseModel, Field

class Voter(BaseModel):
    id: Optional[str] = Field(None, description="voter unique ID")
    name: str = Field(..., description="voter name")
    cc: int = Field(..., description="voter cc")
    email: str = Field(..., description="voter email")
    has_voted: bool = Field(False, description="has the voter voted in the election")

class VoterCreate(BaseModel):
    name: str = Field(..., description="voter name")
    cc: int = Field(..., description="voter cc")
    email: str = Field(..., description="voter email")

class VoterInfo(BaseModel):
    id: str = Field(..., description="voter unique ID")
    name: str = Field(..., description="voter name")

class VoterList(BaseModel):
    voters: List[VoterInfo] = Field(..., description="list of voters")