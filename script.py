# Simulating a database
database = {
    "users": {
        "1": {"phone": "123-456-7890"},
    }
}

# Expected CSRF token
EXPECTED_CSRF_TOKEN = "secure_csrf_token"

def change_user_phone(request_details: dict) -> bool:
    user_id = request_details["body"]["user_id"]
    updated_phone = request_details["body"]["new_phone"]

    if user_id in database["users"]:
        database["users"][user_id]["phone"] = updated_phone
        return True
    else:
        return False
    return False