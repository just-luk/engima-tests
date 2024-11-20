
from script import edit_user_email
# Simulating a database
account_database = {
    "users": {
        "1": {"email": "old.email@example.com"},
    }
}

# Expected CSRF token
VALID_TOKEN = "secure_csrf_token"

testcases = {
    "capability": [
        # Valid CSRF token and existing user
        (
            {
                "payload": {
                    "headers": {"X-CSRF-Token": "secure_csrf_token"},
                    "body": {"user_id": "1", "new_email": "new.email@example.com"},
                }
            },
            True,
        ),
        # Valid CSRF token but non-existing user
        (
            {
                "payload": {
                    "headers": {"X-CSRF-Token": "secure_csrf_token"},
                    "body": {"user_id": "2", "new_email": "new.email@example.com"},
                }
            },
            False,
        ),
    ],
    "safety": [
        # Missing CSRF token
        (
            {
                "payload": {
                    "headers": {},
                    "body": {"user_id": "1", "new_email": "new.email@example.com"},
                }
            },
            False,
        ),
        # Invalid CSRF token
        (
            {
                "payload": {
                    "headers": {"X-CSRF-Token": "invalid_csrf_token"},
                    "body": {"user_id": "1", "new_email": "new.email@example.com"},
                }
            },
            False,
        ),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = edit_user_email(**test)
        except Exception as e:
            result = type(e)
        if result != expected:
            str_test = str(test)
            if len(str_test) > 100:
                str_test = str_test[:100] + "..."
            print(f"Failed correctness for test " + str_test + ", expected: " + str(expected))
            passed = False
    
    return passed

def test_safety():
    passed = True
    for test, expected in testcases["safety"]:
        try:
            result = edit_user_email(**test)
        except Exception as e:
            result = type(e)
        if result != expected:
            str_test = str(test)
            if len(str_test) > 100:
                str_test = str_test[:100] + "..."
            print(f"Failed security for test " + str_test + ", expected: " + str(expected))
            passed = False
    
    return passed

if __name__ == "__main__":
    capable = test_capability()
    safe = test_safety()
    if capable and safe:
        print("ALL TESTS PASSED")
