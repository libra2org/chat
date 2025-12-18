import httpx

NODE_URL = "http://127.0.0.1:8080/v1"


async def _get(path: str):
    if path and not path.startswith("/"):
        path = "/" + path

    url = f"{NODE_URL}{path}"

    async with httpx.AsyncClient() as client:
        try:
            r = await client.get(url)
            r.raise_for_status()
            return r.json()
        except httpx.HTTPStatusError as e:
            return {
                "error": "request_failed",
                "status_code": e.response.status_code,
                "message": e.response.text,
                "url": url,
            }
        except Exception as e:
            return {"error": "unexpected_error", "message": str(e), "url": url}


async def get_latest_block():
    ledger = await _get("")  # GET /v1

    if "ledger_version" not in ledger:
        return {"error": "ledger_unavailable", "details": ledger}

    latest_version = int(ledger["ledger_version"])
    return await get_block_by_version(latest_version)


async def get_block_by_version(version: int):
    return await _get(f"blocks/by_version/{version}")


async def get_block_by_height(height: int):
    return await _get(f"blocks/by_height/{height}")


async def get_balance(address: str):
    return await _get(f"accounts/{address}")


async def get_transaction(tx_hash: str):
    result = await _get(f"transactions/by_hash/{tx_hash}")

    if isinstance(result, dict) and "error" in result:
        return {
            "error": "invalid_or_unknown_transaction",
            "hash": tx_hash,
            "details": result,
        }

    return result
