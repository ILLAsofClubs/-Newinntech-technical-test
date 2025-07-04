from fastapi import APIRouter, HTTPException
from app.services.candidate_services import (
    register_candidate, get_all_candidates, get_candidate_by_id, delete_candidate
)

from app.models.candidates import (
    CreateCandidate, CandidateInfo, CandidateList, Candidate
)

router = APIRouter()

@router.post("/candidates", response_model=Candidate, tags=["Candidates"])
async def create_candidate_route(candidate: CreateCandidate):
    """
    Endpoint to create a new candidate.
    """
    try:
        return register_candidate(candidate)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/candidates", response_model=CandidateList, tags=["Candidates"])
async def get_all_candidates_route():   
    """
    Endpoint to retrieve all candidates.
    """
    try:
        candidates = get_all_candidates()
        return candidates
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/candidates/{id}", response_model=CandidateInfo, tags=["Candidates"])
async def get_candidate_by_id_route(candidate_id: str):
    """
    Endpoint to retrieve a candidate by their ID.
    """
    try:
        candidate = get_candidate_by_id(candidate_id)
        return candidate
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.delete("/candidates/{id}", tags=["Candidates"])
async def delete_candidate_route(candidate_id: str):
    """
    Endpoint to delete a candidate by their ID.
    """
    try:
        deleted_candidate = delete_candidate(candidate_id)
        return deleted_candidate
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))