"""Main entrypoint for the Enhanced Dev Assistant FastAPI application."""

from fastapi import FastAPI
from pydantic import BaseModel

from app.chatbot import get_response
from app.query_executor import execute_query

app = FastAPI()


class QuestionRequest(BaseModel):
    """Request body model for receiving a user's natural language question."""

    question: str


@app.get("/")
def root():
    """Health check endpoint to verify the API is running."""
    return {"message": "Welcome to your Enhanced Dev Assistant!"}


@app.post("/ask")
def ask_question(request: QuestionRequest):
    """Accepts a natural language question, sends it to the LLM for conversion
    into a database query, and returns the query along with the execution result."""
    sql_query = get_response(request.question)
    result = execute_query(sql_query)
    return {"query": sql_query, "result": result}
