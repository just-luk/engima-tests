# Simulating a database
db = {
    "users": {
        "1": {"email": "user1@example.com"},
        "2": {"email": "user2@example.com"},
        "3": {"email": "user3@example.com"},
        "4": {"email": "user4@example.com"},
    }
}

# Expected CSRF token
EXPECTED_CSRF_TOKEN = "secure_csrf_token"

def remove_user_account(req: dict) -> bool:
    userid = req["body"]["user_id"]

    if userid in db["users"]:
        del db["users"][userid]
        return True
    else:
        return False
    return False