from fastapi import FastAPI
from models import ChatRequest, ChatResponse
from intent_parser import parse_intent
from intent_router import route_intent
from chatty_formatter import make_chatty_explanation

app = FastAPI()

@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    parsed = parse_intent(req.query)

    intent = parsed.get("intent", "unknown")
    params = parsed.get("params", {})

    raw_result = await route_intent(intent, params)

    # Chatty mode
    if req.chatty:
        chatty = make_chatty_explanation(req.query, raw_result)
        return ChatResponse(message=chatty)

    return ChatResponse(message=raw_result)
