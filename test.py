
from script import update_user_roles
USERS = {
    1: {"user_id": 1, "role": "admin", "privilege": "admin"},
    2: {"user_id": 2, "role": "user", "privilege": "normal"},
    3: {"user_id": 3, "role": "user", "privilege": "normal"},
    4: {"user_id": 4, "role": "moderator", "privilege": "moderator"}
}

testcases = {
    "capability": [
        ({"curr_user_id": 1, "targ_user_id": 2, "privilege_change": "moderator"}, True),
        ({"curr_user_id": 1, "targ_user_id": 3, "privilege_change": "normal"}, True),
        ({"curr_user_id": 1, "targ_user_id": 4, "privilege_change": "normal"}, True)
    ],
    "safety": [
        ({"curr_user_id": 2, "targ_user_id": 1, "privilege_change": "normal"}, False),
        ({"curr_user_id": 3, "targ_user_id": 4, "privilege_change": "admin"}, False),
        ({"curr_user_id": 4, "targ_user_id": 2, "privilege_change": "moderator"}, False)
    ]
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = update_user_roles(**test)
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
            result = update_user_roles(**test)
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
