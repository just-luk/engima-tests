import json

def validate_and_parse_json(incoming_req: dict) -> dict:
    try:
        return json.loads(incoming_req["body"])
    except json.decoder.JSONDecodeError:
        raise ValueError("Invalid JSON format")
    return {}