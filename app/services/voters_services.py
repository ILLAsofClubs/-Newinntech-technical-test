from typing import Optional

from app.config.env import MONGODB_CONNECTION_STRING, DB_NAME
from app.models.voters import Voter, CreateVoter, VoterInfo, VoterList
from app.database.mongo_connection import database

def register_voter(new_voter: CreateVoter) -> Voter:
    """
    Create a new voter in the database and return the voter information.
    """

    voter_obj = Voter(
        name=new_voter.name.lower(),
        cc=new_voter.cc,
        email=new_voter.email
    )

    # Check if the voter already exists
    existing_voter = database.find_one_document(
        collection=database.voters,
        query={"cc": voter_obj.cc}
    )

    if existing_voter:
        raise ValueError(f"voter with CC {voter_obj.cc} already exists.")

    # Check if the voter isn´t a candidate
    existing_voter = database.find_one_document(
        collection=database.candidates,
        query={"cc": voter_obj.cc}
    )

    if existing_voter:
        raise ValueError(f"voter with CC {voter_obj.cc} is already registered as a candidate.")

    # insert the voter into the database

    try:
        result = database.insert_one_document(
            collection=database.voters,
            document=voter_obj.dict()
        )
    except Exception as e:
        raise Exception(f"Failed to register voter: {e}")
    
    # Add the ID to the voter object
    voter_obj.id = result.get("id")

    return voter_obj

def get_all_voters() -> VoterList:
    """
    Retrieve all voters from the database and return a list of voter information.
    """
    try:
        voters = database.find_all_documents(
            collection=database.voters
        )
    except Exception as e:
        raise Exception(f"Failed to retrieve voters: {e}")

    voter_list = VoterList(
        voters=[VoterInfo(id=str(voter['id']), name=voter['name'], email=voter['email']) for voter in voters]
    )

    return voter_list

def get_voter_by_id(voter_id: str) -> Voter:
    """
    Get voter details by his ID.
    """
    try:
        voter = database.find_one_document(
            collection=database.voters,
            query={"_id": voter_id}
        )
    except Exception as e:
        raise Exception(f"Failed to retrieve voter: {e}")
    
    voter_info = Voter(
        id=str(voter['_id']),
        name=voter['name'],
        cc=voter['cc'],
        email=voter['email'],
        has_voted=voter.get('has_voted', False)
    )

    return voter_info

def delete_voter(voter_id: Optional[str] = None, cc: Optional[int] = None) -> bool:
    """
    Delete a voter by their ID or CC
    """
    if not voter_id or not cc:
        raise ValueError("Either voter_id or cc must be provided.")

    query = {}
    if voter_id:
        query["_id"] = voter_id
    if cc:
        query["cc"] = cc

    try:
        result = database.voters.delete_one(query)
    except Exception as e:
        raise Exception(f"Failed to delete voter: {e}")

    if result.deleted_count == 0:
        raise ValueError("voter not found.")

    return True