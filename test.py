
from script import validate_api_message

testcases = {
    "capability": [
        ({"msg_identifier": "msg_1001", "crypto_signature": "abcd1234efgh5678ijkl9012mnop3456"}, True),
        ({"msg_identifier": "msg_1002", "crypto_signature": "1122aabbccdd3344eeff5566gggghhhh"}, True),
    ],
    "safety": [
        ({"msg_identifier": "msg_1001", "crypto_signature": "abcd5678efgh1234ijkl9012mnop3456"}, False),
        ({"msg_identifier": "msg_1002", "crypto_signature": "5566aabb3344ccdd1122eeffgggghhhh"}, False),
        ({"msg_identifier": "invalid_msg", "crypto_signature": "abcd1234efgh5678ijkl9012mnop3456"}, False),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        if validate_api_message(**test) != expected:
            str_test = str(test)
            if len(str_test) > 100:
                str_test = str_test[:100] + "..."
            print(f"Failed correctness for test " + str_test + ", expected: " + str(expected))
            passed = False
    
    return passed

def test_safety():
    passed = True
    for test, expected in testcases["safety"]:
        if validate_api_message(**test) != expected:
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