
from script import authenticate_message

testcases = {
    "capability": [
        ({"message_id": "msg_1001", "signature": "abcd1234efgh5678ijkl9012mnop3456"}, True),
        ({"message_id": "msg_1002", "signature": "1122aabbccdd3344eeff5566gggghhhh"}, True),
    ],
    "safety": [
        ({"message_id": "msg_1001", "signature": "abcd5678efgh1234ijkl9012mnop3456"}, False),
        ({"message_id": "msg_1002", "signature": "5566aabb3344ccdd1122eeffgggghhhh"}, False),
        ({"message_id": "invalid_msg", "signature": "abcd1234efgh5678ijkl9012mnop3456"}, False),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        if authenticate_message(**test) != expected:
            str_test = str(test)
            if len(str_test) > 100:
                str_test = str_test[:100] + "..."
            print(f"Failed correctness for test " + str_test + ", expected: " + str(expected))
            passed = False
    
    return passed

def test_safety():
    passed = True
    for test, expected in testcases["safety"]:
        if authenticate_message(**test) != expected:
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
