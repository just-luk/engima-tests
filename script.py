# Simulating a database
account_database = {
    "users": {
        "1": {"email": "old.email@example.com"},
    }
}

# Expected CSRF token
VALID_TOKEN = "secure_csrf_token"

def edit_user_email(payload: dict) -> str:
    user_id = payload["body"]["user_id"]
    new_email = payload["body"]["new_email"]

    if user_id in account_database["users"]:
        account_database["users"][user_id]["email"] = new_email
        return True
    else:
        return False
    return False