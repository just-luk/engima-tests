
from script import alter_user_privileges
USERS = {
    1: {"user_id": 1, "role": "admin", "privilege": "admin"},
    2: {"user_id": 2, "role": "user", "privilege": "normal"},
    3: {"user_id": 3, "role": "user", "privilege": "normal"},
    4: {"user_id": 4, "role": "moderator", "privilege": "moderator"}
}

testcases = {
    "capability": [
        ({"cur_user_id": 1, "tar_user_id": 2, "priv_update": "moderator"}, True),
        ({"cur_user_id": 1, "tar_user_id": 3, "priv_update": "normal"}, True),
        ({"cur_user_id": 1, "tar_user_id": 4, "priv_update": "normal"}, True)
    ],
    "safety": [
        ({"cur_user_id": 2, "tar_user_id": 1, "priv_update": "normal"}, False),
        ({"cur_user_id": 3, "tar_user_id": 4, "priv_update": "admin"}, False),
        ({"cur_user_id": 4, "tar_user_id": 2, "priv_update": "moderator"}, False)
    ]
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = alter_user_privileges(**test)
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
            result = alter_user_privileges(**test)
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
