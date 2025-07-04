from fastapi import FastAPI
from app.config.env import VOTER_API, JWT_SECRET, DB_NAME

description = """
    This API is a RESTful API designed to manage voter registration and election processes.
    It provides endpoints for managing voters, elections, candidates and retrieving voter information.
"""

version = "0.0.1"

app = FastAPI(
    title = VOTER_API,
    description = description,
    version = version,
)
