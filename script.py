# Simulating a database
user_data = {
    "users": {
        "1": {"mobile": "123-456-7891"},
    }
}

# Expected CSRF token
EXPECTED_CSRF_TOKEN = "known_csrf_token"

def alter_user_phone(input: dict) -> bool:
    user_ref = input["body"]["user_id"]
    phone_update = input["body"]["new_phone"]

    if user_ref in user_data["users"]:
        user_data["users"][user_ref]["mobile"] = phone_update
        return True
    else:
        return False
    return False