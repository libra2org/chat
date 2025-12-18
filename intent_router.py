from libra2_client import (
    get_latest_block,
    get_balance,
    get_transaction,
)

async def route_intent(intent: str, params: dict):

    if intent == "latest_block":
        return await get_latest_block()

    if intent == "balance":
        address = params.get("address")
        if not address:
            return {"error": "No address provided"}
        return await get_balance(address)

    if intent == "tx_lookup":
        tx_hash = params.get("hash")
        if not tx_hash:
            return {"error": "No transaction hash provided"}
        return await get_transaction(tx_hash)

    return {"error": f"Unknown intent: {intent}"}
