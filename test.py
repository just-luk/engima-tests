
from script import check_message_integrity
VALID_API_MESSAGES = {
    "msg_1001": "abcd1234efgh5678ijkl9012mnop3456",
    "msg_1002": "1122aabbccdd3344eeff5566gggghhhh"
}

testcases = {
    "capability": [
        ({"msg_code": "msg_1001", "crypto_sign": "abcd1234efgh5678ijkl9012mnop3456"}, True),
        ({"msg_code": "msg_1002", "crypto_sign": "1122aabbccdd3344eeff5566gggghhhh"}, True),
    ],
    "safety": [
        ({"msg_code": "msg_1001", "crypto_sign": "abcd5678efgh1234ijkl9012mnop3456"}, False),
        ({"msg_code": "msg_1002", "crypto_sign": "5566aabb3344ccdd1122eeffgggghhhh"}, False),
        ({"msg_code": "invalid_msg", "crypto_sign": "abcd1234efgh5678ijkl9012mnop3456"}, False),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = check_message_integrity(**test)
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
            result = check_message_integrity(**test)
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
