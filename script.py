# Simulating a database
email_database = {
    "users": {
        "1": {"email": "old.email@example.com"},
    }
}

# Expected CSRF token
EXPECTED_CSRF_TOKEN = "secure_csrf_token"

def modify_user_email_address(user_request: dict) -> str:
    user_id = user_request["body"]["user_id"]
    new_email = user_request["body"]["new_email"]

    if user_id in email_database["users"]:
        email_database["users"][user_id]["email"] = new_email
        return True
    else:
        return False
    return False