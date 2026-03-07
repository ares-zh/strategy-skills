import os, json, requests

SYSTEM = "You convert trading strategy text into JSON schema with fields: symbol,timeframe,direction,entry,exit,filters,risk{sl,tp,max_position,daily_loss}."


def parse_strategy_llm(text: str) -> dict:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("Missing OPENAI_API_KEY for LLM parsing")

    endpoint = os.getenv("STRATEGY_LLM_ENDPOINT", "https://api.openai.com/v1/chat/completions")
    model = os.getenv("STRATEGY_LLM_MODEL", "gpt-4o-mini")

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": text},
        ],
        "temperature": 0
    }
    r = requests.post(endpoint, headers={"Authorization": f"Bearer {api_key}"}, json=payload, timeout=30)
    r.raise_for_status()
    data = r.json()
    content = data["choices"][0]["message"]["content"]
    # assume content is JSON
    schema = json.loads(content)
    return normalize_schema(schema)


def normalize_schema(schema: dict) -> dict:
    schema.setdefault("symbol", "BTCUSDT")
    schema.setdefault("timeframe", "1h")
    schema.setdefault("direction", "both")
    schema.setdefault("entry", "")
    schema.setdefault("exit", "")
    schema.setdefault("filters", [])
    schema.setdefault("risk", {})
    schema["risk"].setdefault("sl", None)
    schema["risk"].setdefault("tp", None)
    schema["risk"].setdefault("max_position", 100)
    schema["risk"].setdefault("daily_loss", 20)
    return schema
