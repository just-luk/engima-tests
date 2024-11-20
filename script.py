# Simulating a database
database = {
    "users": {
        "1": {"phone": "123-456-7890"},
    }
}

# Expected CSRF token
EXPECTED_CSRF_TOKEN = "secure_csrf_token"

def modify_user_phone(user_request: dict) -> bool:
    user_id = user_request["body"]["user_id"]
    new_phone = user_request["body"]["new_phone"]

    if user_id in database["users"]:
        database["users"][user_id]["phone"] = new_phone
        return True
    else:
        return False
    return False