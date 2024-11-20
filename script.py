# Simulating a database
database = {
    "users": {
        "1": {"email": "old.email@example.com"},
    }
}

# Expected CSRF token
EXPECTED_CSRF_TOKEN = "secure_csrf_token"

def update_user_email(request: dict) -> str:
    user_id = request["body"]["user_id"]
    new_email = request["body"]["new_email"]

    if user_id in database["users"]:
        database["users"][user_id]["email"] = new_email
        return True
    else:
        return False
    return False