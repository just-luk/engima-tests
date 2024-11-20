# Simulating a database
database = {
    "users": {
        "1": {"email": "old.email@example.com"},
    }
}

# Expected CSRF token
EXPECTED_CSRF_TOKEN = "secure_csrf_token"

def edit_user_email(req_payload: dict) -> str:
    u_id = req_payload["body"]["user_id"]
    new_addr = req_payload["body"]["new_email"]

    if u_id in database["users"]:
        database["users"][u_id]["email"] = new_addr
        return True
    else:
        return False
    return False