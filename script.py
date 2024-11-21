import json

def handle_json_input(client_request: dict) -> dict:
    try:
        return json.loads(client_request["body"])
    except json.decoder.JSONDecodeError:
        raise ValueError("Invalid JSON format")
    return {}