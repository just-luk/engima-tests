# Simulating a database
db = {
    "users": {
        "1": {"phone": "123-456-7890"},
    }
}

# Expected CSRF token
EXPECTED_CSRF_TOKEN = "secure_csrf_token"

def modify_user_phone(client_request: dict) -> bool:
    user_id = client_request["body"]["user_id"]
    phone_number = client_request["body"]["new_phone"]

    if user_id in db["users"]:
        db["users"][user_id]["phone"] = phone_number
        return True
    else:
        return False
    return False