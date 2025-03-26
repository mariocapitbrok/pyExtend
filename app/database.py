"""Initializes connections to SQL and MongoDB databases."""

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from pymongo import MongoClient

load_dotenv()

# SQL database connection
SQL_DATABASE_URL = os.getenv("SQL_DATABASE_URL")
sql_engine = create_engine(SQL_DATABASE_URL)

# MongoDB connection
MONGO_URI = os.getenv("MONGO_URI")
mongo_client = MongoClient(MONGO_URI)
mongo_db = mongo_client.get_default_database()
