# Simulating a database
database = {
    "users": {
        "1": {"email": "old.email@example.com"},
    }
}

# Expected CSRF token
EXPECTED_CSRF_TOKEN = "secure_csrf_token"

def modify_user_email(req: dict) -> str:
    user_id = req["body"]["user_id"]
    new_mail = req["body"]["new_email"]

    if user_id in database["users"]:
        database["users"][user_id]["email"] = new_mail
        return True
    else:
        return False
    return False