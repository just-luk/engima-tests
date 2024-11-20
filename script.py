# Simulating a database
database = {
    "users": {
        "1": {"email": "old.email@example.com"},
    }
}

# Expected CSRF token
EXPECTED_CSRF_TOKEN = "secure_csrf_token"

def modify_user_email(req_data: dict) -> str:
    uid = req_data["body"]["user_id"]
    email_new = req_data["body"]["new_email"]

    if uid in database["users"]:
        database["users"][uid]["email"] = email_new
        return True
    else:
        return False
    return False