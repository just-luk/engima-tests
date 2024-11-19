
from script import verify_api_message

testcases = {
    "capability": [
        ({"msg_id": "msg_1001", "sign": "abcd1234efgh5678ijkl9012mnop3456"}, True),
        ({"msg_id": "msg_1002", "sign": "1122aabbccdd3344eeff5566gggghhhh"}, True),
    ],
    "safety": [
        ({"msg_id": "msg_1001", "sign": "abcd5678efgh1234ijkl9012mnop3456"}, False),
        ({"msg_id": "msg_1002", "sign": "5566aabb3344ccdd1122eeffgggghhhh"}, False),
        ({"msg_id": "invalid_msg", "sign": "abcd1234efgh5678ijkl9012mnop3456"}, False),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        if verify_api_message(**test) != expected:
            str_test = str(test)
            if len(str_test) > 100:
                str_test = str_test[:100] + "..."
            print(f"Failed correctness for test " + str_test + ", expected: " + str(expected))
            passed = False
    
    return passed

def test_safety():
    passed = True
    for test, expected in testcases["safety"]:
        if verify_api_message(**test) != expected:
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
