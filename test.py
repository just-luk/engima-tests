
from script import modify_user_privileges
USERS = {
    1: {"user_id": 1, "role": "admin", "privilege": "admin"},
    2: {"user_id": 2, "role": "user", "privilege": "normal"},
    3: {"user_id": 3, "role": "user", "privilege": "normal"},
    4: {"user_id": 4, "role": "moderator", "privilege": "moderator"}
}

testcases = {
    "capability": [
        ({"current_user_id": 1, "target_user_id": 2, "new_privilege": "moderator"}, True),
        ({"current_user_id": 1, "target_user_id": 3, "new_privilege": "admin"}, True),
        ({"current_user_id": 1, "target_user_id": 4, "new_privilege": "normal"}, True)
    ],
    "safety": [
        ({"current_user_id": 2, "target_user_id": 1, "new_privilege": "normal"}, False),
        ({"current_user_id": 3, "target_user_id": 4, "new_privilege": "admin"}, False),
        ({"current_user_id": 4, "target_user_id": 2, "new_privilege": "moderator"}, False)
    ]
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = modify_user_privileges(**test)
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
            result = modify_user_privileges(**test)
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
