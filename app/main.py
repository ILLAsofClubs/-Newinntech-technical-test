from fastapi import FastAPI
from app.config.env import VOTER_API, JWT_SECRET, DB_NAME
from app.routes.candidate_routes import router as candidate_router
from app.routes.voter_routes import router as voter_router
from app.routes.votes_routes import router as votes_router

description = """
    This API is a RESTful API designed to manage voter registration and election processes.
    It provides endpoints for managing voters, elections, candidates and retrieving voter information.
"""

version = "0.0.1"

app = FastAPI(
    title = VOTER_API,
    description = description,
    version = version,
    docs_url=f"/{VOTER_API}/v1/docs"
)

app.include_router(candidate_router, prefix=f"/{VOTER_API}/v1")
app.include_router(voter_router, prefix=f"/{VOTER_API}/v1")
app.include_router(votes_router, prefix=f"/{VOTER_API}/v1")