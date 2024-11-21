import json

def decode_json_request(req: dict) -> dict:
    try:
        return json.loads(req["body"])
    except json.decoder.JSONDecodeError:
        raise ValueError("Invalid JSON format")
    return {}