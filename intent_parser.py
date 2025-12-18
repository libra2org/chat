import json
import os
from dotenv import load_dotenv
import openai

load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY")

openai.api_base = os.getenv("OPENROUTER_API_BASE")

SYSTEM_PROMPT = """
You are an intent parser for a Libra2 blockchain chatbot.

You must ALWAYS respond with ONLY valid JSON and nothing else.
Your JSON must have exactly:
- "intent": one of ["latest_block", "balance", "tx_lookup"]
- "params": an object with extracted parameters (or {})

Examples:

User: "show me the latest block"
{"intent": "latest_block", "params": {}}

User: "what is the balance of 0x1"
{"intent": "balance", "params": {"address": "0x1"}}

User: "lookup transaction 0xabc"
{"intent": "tx_lookup", "params": {"hash": "0xabc"}}
"""


def parse_intent(query: str):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or any model
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": query},
            ],
            temperature=0,
        )

        content = response["choices"][0]["message"]["content"]
        return json.loads(content)

    except Exception as e:
        print("Intent parser error:", e)
        return {"intent": "unknown", "params": {}}
