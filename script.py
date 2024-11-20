import json

def validate_json_request(input_data: dict) -> dict:
    try:
        return json.loads(input_data["body"])
    except json.decoder.JSONDecodeError:
        raise ValueError("Invalid JSON format")
    return {}