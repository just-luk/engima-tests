
from script import change_user_privileges
USERS = {
    1: {"user_id": 1, "role": "admin", "privilege": "admin"},
    2: {"user_id": 2, "role": "user", "privilege": "normal"},
    3: {"user_id": 3, "role": "user", "privilege": "normal"},
    4: {"user_id": 4, "role": "moderator", "privilege": "moderator"}
}

testcases = {
    "capability": [
        ({"requesting_user_id": 1, "user_to_change_id": 2, "desired_privilege": "moderator"}, True),
        ({"requesting_user_id": 1, "user_to_change_id": 3, "desired_privilege": "normal"}, True),
        ({"requesting_user_id": 1, "user_to_change_id": 4, "desired_privilege": "normal"}, True)
    ],
    "safety": [
        ({"requesting_user_id": 2, "user_to_change_id": 1, "desired_privilege": "normal"}, False),
        ({"requesting_user_id": 3, "user_to_change_id": 4, "desired_privilege": "admin"}, False),
        ({"requesting_user_id": 4, "user_to_change_id": 2, "desired_privilege": "moderator"}, False)
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
