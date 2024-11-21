
from script import get_user_profile
USERS = {
    1: {"user_id": 1, "role": "admin"},
    2: {"user_id": 2, "role": "user"},
    3: {"user_id": 3, "role": "user"},
    4: {"user_id": 4, "role": "user"}
}

USER_PROFILES = {
    1: {"name": "Admin", "email": "admin@example.com"},
    2: {"name": "User2", "email": "user2@example.com"},
    3: {"name": "User3", "email": "user3@example.com"},
    4: {"name": "User4", "email": "user4@example.com"}
}

testcases = {
    "capability": [
        ({"actor_user_id": 1, "requested_user_id": 2}, {"name": "User2", "email": "user2@example.com"}),
        ({"actor_user_id": 2, "requested_user_id": 2}, {"name": "User2", "email": "user2@example.com"}),
        ({"actor_user_id": 3, "requested_user_id": 3}, {"name": "User3", "email": "user3@example.com"}),
    ],
    "safety": [
        ({"actor_user_id": 2, "requested_user_id": 3}, "Unauthorized"),
        ({"actor_user_id": 3, "requested_user_id": 2}, "Unauthorized"),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = get_user_profile(**test)
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
            result = get_user_profile(**test)
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
