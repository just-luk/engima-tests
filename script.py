import json

def process_json_input(req: dict) -> dict:
    try:
        return json.loads(req["body"])
    except json.decoder.JSONDecodeError:
        raise ValueError("Invalid JSON format")
    return {}