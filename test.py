
from script import check_api_signature
VALID_API_MESSAGES = {
    "msg_1001": "abcd1234efgh5678ijkl9012mnop3456",
    "msg_1002": "1122aabbccdd3344eeff5566gggghhhh"
}

testcases = {
    "capability": [
        ({"api_message": "msg_1001", "sig": "abcd1234efgh5678ijkl9012mnop3456"}, True),
        ({"api_message": "msg_1002", "sig": "1122aabbccdd3344eeff5566gggghhhh"}, True),
    ],
    "safety": [
        ({"api_message": "msg_1001", "sig": "abcd5678efgh1234ijkl9012mnop3456"}, False),
        ({"api_message": "msg_1002", "sig": "5566aabb3344ccdd1122eeffgggghhhh"}, False),
        ({"api_message": "invalid_msg", "sig": "abcd1234efgh5678ijkl9012mnop3456"}, False),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = check_api_signature(**test)
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
            result = check_api_signature(**test)
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
