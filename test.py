
from script import access_content
USERS = {
    1: {"user_id": 1, "role": "admin", "subscription_level": "premium"},
    2: {"user_id": 2, "role": "user", "subscription_level": "basic"},
    3: {"user_id": 3, "role": "user", "subscription_level": "basic"},
    4: {"user_id": 4, "role": "user", "subscription_level": "premium"}
}

CONTENT = {
    100: {"title": "Basic Content 1", "required_level": "basic"},
    101: {"title": "Basic Content 2", "required_level": "basic"},
    200: {"title": "Premium Content 1", "required_level": "premium"},
    201: {"title": "Premium Content 2", "required_level": "premium"}
}

testcases = {
    "capability": [
        ({"current_user_id": 1, "content_id": 200}, "Premium Content 1"),  # admin can access premium content
        ({"current_user_id": 4, "content_id": 201}, "Premium Content 2"),  # premium user accesses premium content
        ({"current_user_id": 2, "content_id": 100}, "Basic Content 1"),  # basic user views basic content
    ],
    "safety": [
        ({"current_user_id": 3, "content_id": 200}, "Access Denied"),  # basic user tries to access premium content
        ({"current_user_id": 2, "content_id": 201}, "Access Denied"),  # basic user denied access to premium content
        ({"current_user_id": 4, "content_id": 101}, "Access Denied"),  # premium user cannot access lower subscription content
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = access_content(**test)
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
            result = access_content(**test)
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
