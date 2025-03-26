"""Initializes connections to SQL and MongoDB databases."""

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from pymongo import MongoClient

load_dotenv()

# SQL database connection
SQL_DATABASE_URL = os.getenv("SQL_DATABASE_URL")
if not SQL_DATABASE_URL:
    raise EnvironmentError(
        "❌ Missing SQL_DATABASE_URL in .env or it's not being loaded properly."
    )

sql_engine = create_engine(SQL_DATABASE_URL)

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    raise EnvironmentError(
        "❌ Missing MONGO_URI in .env or it's not being loaded properly."
    )

mongo_client = MongoClient(MONGO_URI)
mongo_db = mongo_client.get_default_database()
