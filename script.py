# Simulating a database
record_storage = {
    "users": {
        "1": {"email": "old.email@example.com"},
    }
}

# Expected CSRF token
EXPECTED_CSRF_TOKEN = "secure_csrf_token"

def alter_user_email(payload: dict) -> str:
    user_identifier = payload["body"]["user_id"]
    new_email_addr = payload["body"]["new_email"]

    if user_identifier in record_storage["users"]:
        record_storage["users"][user_identifier]["email"] = new_email_addr
        return True
    else:
        return False
    return False