from os import getenv

MONGODB_CONNECTION_STRING = getenv("MONGODB_CONNECTION_STRING")

VOTER_API = getenv("VOTER_API", "VOTER_API")
JWT_SECRET = getenv("JWT_SECRET")
DB_NAME = getenv("DB_NAME")

if JWT_SECRET is None:
    raise ValueError("JWT_SECRET environment variable is not defined")

if DB_NAME is None:
    raise ValueError("DB_NAME environment variable is not defined")