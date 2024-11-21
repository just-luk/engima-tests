import json

def parse_json_request(request: dict) -> dict:
    try:
        return json.loads(request["body"])
    except json.decoder.JSONDecodeError:
        raise ValueError("Invalid JSON format")
    return {}