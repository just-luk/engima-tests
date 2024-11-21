# Simulating a database
db_users = {
    "users": {
        "1": {"telephone": "123-556-7890"},
    }
}

# Expected CSRF token
EXPECTED_CSRF_TOKEN = "csrf_token_secured"

def change_user_phone(payload: dict) -> bool:
    user_key = payload["body"]["user_id"]
    new_number = payload["body"]["new_phone"]

    if user_key in db_users["users"]:
        db_users["users"][user_key]["telephone"] = new_number
        return True
    else:
        return False
    return False