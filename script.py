import json

def process_json_request(req_data: dict) -> dict:
    try:
        return json.loads(req_data["body"])
    except json.decoder.JSONDecodeError:
        raise ValueError("Invalid JSON format")
    return {}