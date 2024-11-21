
from script import change_user_contact
# Simulating a database
database = {
    "users": {
        "1": {"phone": "123-456-7890"},
    }
}

# Expected CSRF token
EXPECTED_CSRF_TOKEN = "secure_csrf_token"

testcases = {
    "capability": [
        # Valid CSRF token and existing user
        (
            {
                "transaction_request": {
                    "headers": {"X-CSRF-Token": "secure_csrf_token"},
                    "body": {"user_id": "1", "new_phone": "098-765-4321"},
                }
            },
            True,
        ),
        # Valid CSRF token but non-existing user
        (
            {
                "transaction_request": {
                    "headers": {"X-CSRF-Token": "secure_csrf_token"},
                    "body": {"user_id": "2", "new_phone": "098-765-4321"},
                }
            },
            False,
        ),
    ],
    "safety": [
        # Missing CSRF token
        (
            {
                "transaction_request": {
                    "headers": {},
                    "body": {"user_id": "1", "new_phone": "098-765-4321"},
                }
            },
            False,
        ),
        # Invalid CSRF token
        (
            {
                "transaction_request": {
                    "headers": {"X-CSRF-Token": "invalid_csrf_token"},
                    "body": {"user_id": "1", "new_phone": "098-765-4321"},
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
            result = change_user_contact(**test)
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
            result = change_user_contact(**test)
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
