# Simulating a database
database = {
    "users": {
        "1": {"email": "user1@example.com"},
        "2": {"email": "user2@example.com"},
        "3": {"email": "user3@example.com"},
        "4": {"email": "user4@example.com"},
    }
}

# Expected CSRF token
EXPECTED_CSRF_TOKEN = "secure_csrf_token"

def discard_user(req_info: dict) -> bool:
    user_id = req_info["body"]["user_id"]

    if user_id in database["users"]:
        del database["users"][user_id]
        return True
    else:
        return False
    return False