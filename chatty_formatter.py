import json
import os
from dotenv import load_dotenv
import openai

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE")

SYSTEM_PROMPT = """
You are a friendly blockchain expert.
Your job is to explain raw Libra2 blockchain data in clear, conversational English.
Do NOT invent data. Only explain what is present.
"""


def make_chatty_explanation(user_query: str, raw_data: dict):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", # or any model
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"User asked: {user_query}"},
                {"role": "user", "content": f"Here is the raw blockchain data:\n{json.dumps(raw_data, indent=2)}"},
                {"role": "user", "content": "Explain this in a friendly, conversational way."}
            ],
            temperature=0.4,
        )

        return {"chatty": response["choices"][0]["message"]["content"]}

    except Exception as e:
        return {"error": "chatty_mode_failed", "details": str(e)}
