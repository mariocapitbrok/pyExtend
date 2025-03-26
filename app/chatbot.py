"""Handles interaction with the OpenAI API to convert natural language to queries."""

import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


# pylint: disable=no-member
def get_response(question: str) -> str:
    """
    Converts a natural language question into an SQL query using OpenAI.
    Args:
        question (str): The user's question in plain English.
    Returns:
        str: A generated SQL query as a string.
    """
    prompt = f"Translate the following question into an SQL query: '{question}'"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )

    return response["choices"][0]["message"]["content"].strip()
