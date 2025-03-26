"""Test connection to PostgreSQL and MongoDB."""

from sqlalchemy import text
from app.database import sql_engine, mongo_db


def test_postgres():
    """Tests connection to PostgreSQL by running a simple SELECT 1."""
    try:
        with sql_engine.connect() as conn:
            result = conn.execute(text("SELECT 1")).scalar()
            print(f"[✅] PostgreSQL connected — SELECT 1 returned: {result}")
    except Exception as e:
        print(f"[❌] PostgreSQL connection failed: {e}")


def test_mongo():
    """Tests connection to MongoDB by inserting and reading a dummy document."""
    try:
        collection = mongo_db["test_connection"]
        doc = {"status": "MongoDB is alive!"}
        inserted_id = collection.insert_one(doc).inserted_id
        result = collection.find_one({"_id": inserted_id})
        print(f"[✅] MongoDB connected — Inserted doc: {result}")
    except Exception as e:
        print(f"[❌] MongoDB connection failed: {e}")


if __name__ == "__main__":
    test_postgres()
    test_mongo()
