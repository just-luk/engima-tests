# Simulating a database
database = {
    "users": {
        "1": {"email": "old.email@example.com"},
    }
}

# Expected CSRF token
EXPECTED_CSRF_TOKEN = "secure_csrf_token"

def change_user_email(query: dict) -> str:
    user_id = query["body"]["user_id"]
    updated_email = query["body"]["new_email"]

    if user_id in database["users"]:
        database["users"][user_id]["email"] = updated_email
        return True
    else:
        return False
    return False