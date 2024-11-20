
from script import retrieve_user_info
TRUSTED_USER_PROFILES = {
    "user_abc": "4e99a098d57cbf9c6f67f176106769fb",
    "user_xyz": "12e4b2f76650484030e4d447d0b5f723"
}


# Simulated function for fetching user profile data from remote service
def get_profile_from_service(uid: str):
    if uid in TRUSTED_USER_PROFILES:
        return {"name": "Test User", "email": f"{uid}@example.com"}
    else:
        raise ConnectionError(f"Could not fetch profile for user_id {uid}")

testcases = {
    "capability": [
        ({"uid": "user_abc", "sig": "4e99a098d57cbf9c6f67f176106769fb"},
         {"name": "Test User", "email": "user_abc@example.com"}),
        ({"uid": "user_xyz", "sig": "12e4b2f76650484030e4d447d0b5f723"},
         {"name": "Test User", "email": "user_xyz@example.com"}),
    ],
    "safety": [
        ({"uid": "user_abc", "sig": "12e4b2f76650484030e4d447d0b5f723"}, None),
        ({"uid": "user_xyz", "sig": "4e99a098d57cbf9c6f67f176106769fb"}, None),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = retrieve_user_info(**test)
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
            result = retrieve_user_info(**test)
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
