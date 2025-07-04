from typing import Optional, List, Dict, Any, Union
from pydantic import BaseModel, Field

class Vote(BaseModel):
    voter_id: str = Field(..., description="ID of the voter who cast the vote")
    candidate_id: str = Field(..., description="ID of the candidate who received the vote")

class RegisterVote(BaseModel):
    voter_id: str = Field(..., description="ID of the voter who is casting the vote")
    candidate_id: str = Field(..., description="ID of the candidate who is receiving the vote")

class VoteList(BaseModel):
    votes = List[Vote] = Field(..., description="list of votes cast in the election")

class TotalVotesPerCandidate(BaseModel):
    candidate_id: str = Field(..., description="ID of the candidate for whom the total votes are being counted")
    percentage: float = Field(..., description="Percentage of total votes received by the candidate")
    total_votes: int = Field(..., description="Total number of votes cast in the election")

class VoteStatistics(BaseModel):
    total_votes_per_candidate: List[TotalVotesPerCandidate] = Field(..., description="List of total votes per candidate, including percentage and total votes")
    total_voters: int = Field(..., description="Total number of voters who have cast their votes in the election")    