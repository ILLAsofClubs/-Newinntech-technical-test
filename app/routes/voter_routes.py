from fastapi import APIRouter, HTTPException
from app.services.voters_services import (
    register_voter, get_all_voters, get_voter_by_id, delete_voter
)
from app.models.voters import (
    VoterCreate, VoterInfo, VoterList, Voter
)

router = APIRouter()

@router.post("/voters", response_model=Voter, tags=["Voters"])
async def create_voter_route(voter: VoterCreate):
    """
    Endpoint to create a new voter.
    """
    try:
        return register_voter(voter)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/voters", response_model=VoterList, tags=["Voters"])
async def get_all_voters_route():
    """
    Endpoint to retrieve all voters.
    """
    try:
        voters = get_all_voters()
        return voters
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/voters/{id}", response_model=VoterInfo, tags=["Voters"])
async def get_voter_by_id_route(voter_id: str):
    """
    Endpoint to retrieve a voter by their ID.
    """
    try:
        voter = get_voter_by_id(voter_id)
        return voter
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.delete("/voters/{id}", tags=["Voters"])
async def delete_voter_route(voter_id: str):
    """
    Endpoint to delete a voter by their ID.
    """
    try:
        deleted_voter = delete_voter(voter_id)
        return deleted_voter
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))