from typing import Optional

from app.config.env import MONGODB_CONNECTION_STRING, DB_NAME
from app.models.candidates import Candidate, CreateCandidate, CandidateInfo, CandidateList
from app.database.mongo_connection import database

from bson import ObjectId

def register_candidate(new_candidate: CreateCandidate) -> Candidate:
    """
    Create a new candidate in the database and return the candidate information.
    """

    candidate_obj = Candidate(
        name=new_candidate.name.lower(),
        cc=new_candidate.cc,
        party=new_candidate.party
    )

    # Check if the candidate already exists
    existing_candidate = database.find_one_document(
        collection=database.candidates,
        query={"cc": candidate_obj.cc}
    )

    if existing_candidate:
        raise ValueError(f"Candidate with CC {candidate_obj.cc} already exists.")

    # Check if the candidate isn´t a voter
    existing_candidate = database.find_one_document(
        collection=database.voters,
        query={"cc": candidate_obj.cc}
    )

    if existing_candidate:
        raise ValueError(f"Candidate with CC {candidate_obj.cc} is already registered as a voter.")

    # insert the candidate into the database

    try:
        result = database.insert_one_document(
            collection=database.candidates,
            document=candidate_obj.dict()
        )
    except Exception as e:
        raise Exception(f"Failed to register candidate: {e}")
    
    # Add the ID to the candidate object
    candidate_obj.id = result.get("id")

    return candidate_obj

def get_all_candidates() -> CandidateList:
    """
    Retrieve all candidates from the database and return a list of candidate information.
    """
    try:
        candidates = database.find_all_documents(
            collection=database.candidates
        )
    except Exception as e:
        raise Exception(f"Failed to retrieve candidates: {e}")

    candidates_info = []
    for candidate in candidates:
        candidates_info.append(
            CandidateInfo(
                id=str(candidate['_id']),
                name=candidate['name'],
                party=candidate['party'],

            )
        )
    
    candidate_list = CandidateList(
        candidates=candidates_info
    )

    return candidate_list

def get_candidate_by_id(candidate_id: str) -> Candidate:
    """
    Get candidate details by his ID.
    """
    try:
        candidate = database.find_one_document(
            collection=database.candidates,
            query={"_id": ObjectId(candidate_id)}
        )
        print(candidate)
    except Exception as e:
        raise Exception(f"Failed to retrieve candidate: {e}")
    
    candidate_info = Candidate(
        id=str(candidate['_id']),
        name=candidate['name'],
        cc=candidate['cc'],
        party=candidate['party'],
        votes=candidate.get('votes', 0)  # Default to 0 if 'votes' key is not present
    )

    return candidate_info

def delete_candidate(candidate_id: Optional[str] = None, cc: Optional[int] = None) -> bool:
    """
    Delete a candidate by their ID or CC
    """
    if not candidate_id and not cc:
        raise ValueError("Either candidate_id or cc must be provided.")

    query = {}
    if candidate_id:
        query["_id"] = ObjectId(candidate_id)
    if cc:
        query["cc"] = cc

    try:
        result = database.candidates.delete_one(query)
        print(result)
    except Exception as e:
        raise Exception(f"Failed to delete candidate: {e}")

    if result.deleted_count == 0:
        raise ValueError("Candidate not found.")

    return True