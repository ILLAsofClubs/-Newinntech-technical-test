from typing import List

from app.models.voters import Voter
from app.models.candidates import Candidate
from app.models.vote import Vote, RegisterVote, TotalVotesPerCandidate, VoteStatistics

from bson import ObjectId

from app.database.mongo_connection import database

def register_vote(vote_data: RegisterVote) -> Vote:
    """
    Validate if the voter and candidate exist, then register the vote.
    """

    # check if the voter exists
    voter = database.find_one_document(
        collection=database.voters,
        query={"_id": ObjectId(vote_data.voter_id)}
    )

    if not voter:
        raise ValueError(f"Voter with ID {vote_data.voter_id} does not exist.")
    
    # check if the candidate exists
    candidate = database.find_one_document(
        collection=database.candidates,
        query={"_id": ObjectId(vote_data.candidate_id)}
    )

    if not candidate:
        raise ValueError(f"Candidate with ID {vote_data.candidate_id} does not exist.")
    
    vote = Vote(
        voter_id=vote_data.voter_id,
        candidate_id=vote_data.candidate_id
    )

    try:
        # check if the voter has already voted
        existing_vote = database.find_one_document(
            collection=database.votes,
            query={"voter_id": vote_data.voter_id}
        )
        
        if existing_vote:
            raise ValueError(f"Voter with ID {vote_data.voter_id} has already voted.")
    except Exception as e:
        raise Exception(f"Failed to check if voter has already voted: {e}")

    # insert the vote into the database
    try:
        result = database.insert_one_document(
            collection=database.votes,
            document=vote.dict()
        )
    except Exception as e:
        raise Exception(f"Failed to register vote: {e}")
    
    try:
        # update the voter's has_voted status
        database.voters.update_one(
            {"_id": ObjectId(vote_data.voter_id)},
            {"$set": {"has_voted": True}}
        )
    except Exception as e:
        raise Exception(f"Failed to update voter's has_voted status: {e}")
    
    try:
        # update the candidate's votes count
        database.candidates.update_one(
            {"_id": ObjectId(vote_data.candidate_id)},
            {"$inc": {"votes": 1}}
        )
    except Exception as e:
        raise Exception(f"Failed to update candidate's votes count: {e}")

    return vote

def get_all_votes() -> List[Vote]:
    """
    get all votes from the database.
    """

    try:
        votes = list(database.find_all_documents(
            collection=database.votes,
            query={}
        ))
    except Exception as e:
        raise Exception(f"Failed to retrieve votes: {e}")


    return [Vote(voter_id=vote["voter_id"], candidate_id=vote["candidate_id"] ) for vote in votes]

def get_votes_statistics() -> VoteStatistics:
    """
    Get the statistics of votes, including total votes and votes per candidate.
    """

    # get all votes
    try:
        votes = get_all_votes()
    except Exception as e:  
        raise Exception(f"Failed to retrieve votes: {e}")
    
    total_votes = len(votes)

    # get total candidates
    try:
        candidates = list(database.find_all_documents(
            collection=database.candidates,
            query={}
        ))
    except Exception as e:
        raise Exception(f"Failed to retrieve candidates: {e}")
    

    total_votes_per_candidate = []
    for candidate in candidates:
        percentage = ((candidate.get('votes', 0) / total_votes) * 100) if total_votes > 0 else 0

        total_votes_per_candidate.append(
            TotalVotesPerCandidate(
                candidate_id=str(candidate['_id']),
                percentage=percentage,
                total_votes=candidate.get('votes', 0)
            )
        )
    
    total_voters = list(database.find_all_documents(collection=database.voters))
    
    votes_statistics = VoteStatistics(
        total_votes_per_candidate=total_votes_per_candidate,
        total_voters=len(total_voters)
    )

    return votes_statistics


