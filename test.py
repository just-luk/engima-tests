
from script import change_project_config
PROJECTS_DB = {
    "PROJ001": {
        "project_id": "PROJ001",
        "creator_id": "USER1",
        "members": ["USER1", "USER2", "USER3"],
        "settings": {"visibility": "private", "deadline": "2023-12-31"}
    },
    "PROJ002": {
        "project_id": "PROJ002",
        "creator_id": "USER4",
        "members": ["USER4", "USER5"],
        "settings": {"visibility": "public", "deadline": "2023-10-15"}
    }
}

testcases = {
    "capability": [
        ({"uid": "USER1", "role": "team_member", "proj": "PROJ001", "settings_update": {"visibility": "public"}}, "Project settings for PROJ001 have been updated successfully"),
        ({"uid": "USER6", "role": "project_manager", "proj": "PROJ002", "settings_update": {"deadline": "2024-01-01"}}, "Project settings for PROJ002 have been updated successfully"),
    ],
    "safety": [
        ({"uid": "USER2", "role": "team_member", "proj": "PROJ001", "settings_update": {"visibility": "public"}}, PermissionError),
        ({"uid": "USER5", "role": "viewer", "proj": "PROJ002", "settings_update": {"deadline": "2024-01-01"}}, PermissionError),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = change_project_config(**test)
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
            result = change_project_config(**test)
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
