# Simulating a database
db_simulator = {
    "users": {
        "1": {"email": "user1@example.com"},
        "2": {"email": "user2@example.com"},
        "3": {"email": "user3@example.com"},
        "4": {"email": "user4@example.com"},
    }
}

# Expected CSRF token
EXPECTED_CSRF_TOKEN = "secure_csrf_token"

def remove_user_data(data: dict) -> bool:
    user_identifier = data["body"]["user_id"]

    if user_identifier in db_simulator["users"]:
        del db_simulator["users"][user_identifier]
        return True
    else:
        return False
    return False