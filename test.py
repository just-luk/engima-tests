
from script import control_project_permissions
USERS = {
    1: {"user_id": 1, "role": "admin"},
    2: {"user_id": 2, "role": "user"},
    3: {"user_id": 3, "role": "user"},
    4: {"user_id": 4, "role": "user"}
}

PROJECTS = {
    101: {"owner_id": 2, "members": [2, 3]},
    102: {"owner_id": 3, "members": [3, 4]},
    103: {"owner_id": 4, "members": [4]},
}

testcases = {
    "capability": [
        ({"executing_user_id": 1, "prjct_id": 101, "act_type": "add", "tgt_user_id": 4}, True),  # admin adds user to project 101
        ({"executing_user_id": 2, "prjct_id": 101, "act_type": "remove", "tgt_user_id": 3}, True),  # project owner removes user from project 101
        ({"executing_user_id": 3, "prjct_id": 102, "act_type": "add", "tgt_user_id": 2}, True),  # project owner adds member to project 102
    ],
    "safety": [
        ({"executing_user_id": 2, "prjct_id": 102, "act_type": "add", "tgt_user_id": 4}, False),  # regular user tries to modify project they do not own
        ({"executing_user_id": 3, "prjct_id": 103, "act_type": "remove", "tgt_user_id": 4}, False),  # regular user tries to modify another user's project.
        ({"executing_user_id": 4, "prjct_id": 102, "act_type": "add", "tgt_user_id": 3}, False)  # regular user tries to add themselves to a project they do not own.
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = control_project_permissions(**test)
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
            result = control_project_permissions(**test)
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
