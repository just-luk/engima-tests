
from script import change_user_privileges
USERS = {
    1: {"user_id": 1, "role": "admin", "privilege": "admin"},
    2: {"user_id": 2, "role": "user", "privilege": "normal"},
    3: {"user_id": 3, "role": "user", "privilege": "normal"},
    4: {"user_id": 4, "role": "moderator", "privilege": "moderator"}
}

testcases = {
    "capability": [
        ({"active_user_id": 1, "affected_user_id": 2, "updated_privilege": "moderator"}, True),
        ({"active_user_id": 1, "affected_user_id": 3, "updated_privilege": "normal"}, True),
        ({"active_user_id": 1, "affected_user_id": 4, "updated_privilege": "normal"}, True)
    ],
    "safety": [
        ({"active_user_id": 2, "affected_user_id": 1, "updated_privilege": "normal"}, False),
        ({"active_user_id": 3, "affected_user_id": 4, "updated_privilege": "admin"}, False),
        ({"active_user_id": 4, "affected_user_id": 2, "updated_privilege": "moderator"}, False)
    ]
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = change_user_privileges(**test)
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
            result = change_user_privileges(**test)
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
