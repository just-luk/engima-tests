import json

def analyze_json_request(incoming_request: dict) -> dict:
    try:
        return json.loads(incoming_request["body"])
    except json.decoder.JSONDecodeError:
        raise ValueError("Invalid JSON format")
    return {}