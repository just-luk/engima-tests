import json

def handle_json_request(http_request: dict) -> dict:
    try:
        return json.loads(http_request["body"])
    except json.decoder.JSONDecodeError:
        raise ValueError("Invalid JSON format")
    return {}