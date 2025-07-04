from app.config.env import MONGODB_CONNECTION_STRING, DB_NAME
from app.models.candidates import Candidate, CreateCandidate, CandidateInfo, CandidateList
from app.database.mongo_connection import database

def register_candidate(new_candidate: CreateCandidate) -> Candidate:
    """
    Create a new candidate in the database and return the candidate information.
    """
    candidate_obj = Candidate(
        name=new_candidate.name,
        party=new_candidate.party
    )
    # insert the candidate into the database

    try:
        result = database.insert_one_document(
            collection=database.candidates,
            document=candidate_obj.dict()
        )
    except Exception as e:
        raise Exception(f"Failed to register candidate: {e}")
    
    # Add the ID to the candidate object
    candidate_obj.id = str(result.inserted_id)

    return candidate_obj