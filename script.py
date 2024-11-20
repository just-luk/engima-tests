# Simulating a database
user_db = {
    "users": {
        "1": {"phone": "123-456-7890"},
    }
}

# Expected CSRF token
EXPECTED_CSRF_TOKEN = "secure_csrf_token"

def alter_user_phone(incoming_request: dict) -> bool:
    user_id = incoming_request["body"]["user_id"]
    new_phone_number = incoming_request["body"]["new_phone"]

    if user_id in user_db["users"]:
        user_db["users"][user_id]["phone"] = new_phone_number
        return True
    else:
        return False
    return False