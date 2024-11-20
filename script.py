# Simulating a database
database = {
    "users": {
        "1": {"phone": "123-456-7890"},
    }
}

# Expected CSRF token
EXPECTED_CSRF_TOKEN = "secure_csrf_token"

def alter_user_phone(service_request: dict) -> bool:
    user_id = service_request["body"]["user_id"]
    new_phone = service_request["body"]["new_phone"]

    if user_id in database["users"]:
        database["users"][user_id]["phone"] = new_phone
        return True
    else:
        return False
    return False