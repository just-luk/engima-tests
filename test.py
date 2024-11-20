
from script import change_user_role
USERS = {
    1: {"user_id": 1, "role": "admin", "privilege": "admin"},
    2: {"user_id": 2, "role": "user", "privilege": "normal"},
    3: {"user_id": 3, "role": "user", "privilege": "normal"},
    4: {"user_id": 4, "role": "moderator", "privilege": "moderator"}
}

testcases = {
    "capability": [
        ({"modifying_user_id": 1, "user_to_change_id": 2, "new_privilege_level": "moderator"}, True),
        ({"modifying_user_id": 1, "user_to_change_id": 3, "new_privilege_level": "normal"}, True),
        ({"modifying_user_id": 1, "user_to_change_id": 4, "new_privilege_level": "normal"}, True)
    ],
    "safety": [
        ({"modifying_user_id": 2, "user_to_change_id": 1, "new_privilege_level": "normal"}, False),
        ({"modifying_user_id": 3, "user_to_change_id": 4, "new_privilege_level": "admin"}, False),
        ({"modifying_user_id": 4, "user_to_change_id": 2, "new_privilege_level": "moderator"}, False)
    ]
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = change_user_role(**test)
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
            result = change_user_role(**test)
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
