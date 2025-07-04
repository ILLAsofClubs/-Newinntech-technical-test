from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.errors import OperationFailure, ConnectionFailure, PyMongoError
from app.config.env import MONGODB_CONNECTION_STRING, DB_NAME

# Initialize MongoDB connection

try:
    client = MongoClient(MONGODB_CONNECTION_STRING)

except (ConnectionFailure, PyMongoError) as e:
    raise ConnectionError(f"Failed to connect to MongoDB: {e}")

# Create a interface for the MongoDB connection
class MongoConnection:

    # Create a constructor to initialize the database and collections
    def __init__(self, db_name: str = DB_NAME) -> None:
        try:
            self.db: Database = client[db_name]
        except OperationFailure as e:
            raise ConnectionError(f"Failed to access database '{db_name}': {e}")
        
        self.candidates: Collection = self.__get_candidate_collection()
        self.voters: Collection = self.__get_voters_collection()
        self.votes: Collection = self.__get_votes_collection()
        
        # Collection methods      
    def __get_candidate_collection(self) -> Collection:

        """
        Get the candidates collection from the database.
        """
        return self.db["candidates"]
    
    def __get_voters_collection(self) -> Collection:

        """
        Get the voters collection from the database.
        """
        return self.db["voters"]
    
    def __get_votes_collection(self) -> Collection:

        """
        Get the votes collection from the database.
        """
        return self.db["votes"]
    
    # Get methods
    def find_one_document(self, collection: Collection, query: dict) -> dict:
        """
        Get a single document from the specified collection based on the query.
        """
        return collection.find_one(query)
    
    def find_all_documents(self, collection: Collection, query: dict = {}) -> list:
        """
        Get all documents from the specified collection based on the query.
        """
        return list(collection.find(query))
    
    # Insert methods
    def insert_one_document(self, collection: Collection, document: dict) -> dict:
        """
        Insert a single document into the specified collection.
        """
        try:
            result = collection.insert_one(document)
            return {"id": str(result.inserted_id)}
        except PyMongoError as e:
            raise Exception(f"Failed to insert document: {e}")

database = MongoConnection()