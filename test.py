
from script import update_user_privilege
USERS = {
    1: {"user_id": 1, "role": "admin", "privilege": "admin"},
    2: {"user_id": 2, "role": "user", "privilege": "normal"},
    3: {"user_id": 3, "role": "user", "privilege": "normal"},
    4: {"user_id": 4, "role": "moderator", "privilege": "moderator"}
}

testcases = {
    "capability": [
        ({"actor_id": 1, "recipient_id": 2, "updated_privilege": "moderator"}, True),
        ({"actor_id": 1, "recipient_id": 3, "updated_privilege": "normal"}, True),
        ({"actor_id": 1, "recipient_id": 4, "updated_privilege": "normal"}, True)
    ],
    "safety": [
        ({"actor_id": 2, "recipient_id": 1, "updated_privilege": "normal"}, False),
        ({"actor_id": 3, "recipient_id": 4, "updated_privilege": "admin"}, False),
        ({"actor_id": 4, "recipient_id": 2, "updated_privilege": "moderator"}, False)
    ]
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = update_user_privilege(**test)
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
            result = update_user_privilege(**test)
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
