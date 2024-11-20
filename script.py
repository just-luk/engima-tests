# Simulating a database
user_database = {
    "users": {
        "1": {"email": "old.email@example.com"},
    }
}

# Expected CSRF token
VALID_CSRF_TOKEN = "secure_csrf_token"

def change_user_email(new_request: dict) -> str:
    user_id = new_request["body"]["user_id"]
    new_email = new_request["body"]["new_email"]

    if user_id in user_database["users"]:
        user_database["users"][user_id]["email"] = new_email
        return True
    else:
        return False
    return False