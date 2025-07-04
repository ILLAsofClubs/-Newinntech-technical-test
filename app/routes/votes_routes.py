from fastapi import APIRouter, HTTPException
from app.services.votes_services import (
    register_vote, get_all_votes, get_votes_statistics
)
from app.models.vote import (
    RegisterVote, VoteList, TotalVotesPerCandidate, VoteStatistics, Vote
)

router = APIRouter()

@router.post("/votes", response_model=Vote, tags=["Votes"])
async def register_vote_route(voter_id: str, candidate_id: str):
    """
    Endpoint to register a vote for a candidate by a voter.
    """
    try:
        return register_vote(
            RegisterVote(voter_id=voter_id, candidate_id=candidate_id)
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/votes", response_model=VoteList, tags=["Votes"])
async def get_all_votes_route():
    """
    Endpoint to retrieve all votes cast in the election.
    """
    try:
        votes = get_all_votes()
        return VoteList(votes=votes)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/votes/statistics", response_model=VoteStatistics, tags=["Votes"])
async def get_votes_statistics_route():
    """
    Endpoint to retrieve the statistics of votes, including total votes and votes per candidate.
    """
    try:
        statistics = get_votes_statistics()
        return statistics
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))