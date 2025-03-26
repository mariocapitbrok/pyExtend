"""Executes SQL queries (MongoDB support coming soon) and returns formatted results."""

import pandas as pd
from sqlalchemy.exc import SQLAlchemyError

from app.database import sql_engine


def execute_query(query: str):
    """
    Executes a SQL query using the configured SQLAlchemy engine.
    Args:
        query (str): The SQL query string to execute.
    Returns:
        list[dict] | dict: Query results as a list of dictionaries,
                           or an error message dictionary.
    """
    try:
        with sql_engine.connect() as connection:
            result = pd.read_sql_query(query, connection)
            return result.to_dict(orient="records")
    except SQLAlchemyError as e:
        return {"error": str(e)}
