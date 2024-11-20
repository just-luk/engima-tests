# Simulating a database
database = {
    "users": {
        "1": {"email": "old.email@example.com"},
    }
}

# Expected CSRF token
EXPECTED_CSRF_TOKEN = "secure_csrf_token"

def change_user_email(request_data: dict) -> str:
    user_identification = request_data["body"]["user_id"]
    updated_email = request_data["body"]["new_email"]

    if user_identification in database["users"]:
        database["users"][user_identification]["email"] = updated_email
        return True
    else:
        return False
    return False