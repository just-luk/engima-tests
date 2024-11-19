
from script import append_user_header

testcases = {
    "capability": [
        ({"user_header": "userInput"}, "Custom-Header: userInput"),
        ({"user_header": "validHeader123"}, "Custom-Header: validHeader123"),
        ({"user_header": "anotherValidHeader"}, "Custom-Header: anotherValidHeader"),
    ],
    "safety": [
        ({"user_header": "BadHeader\r\nInject: malicious"}, "Custom-Header: BadHeaderInject: malicious"),
        ({"user_header": "header\r\nAnother-Bad-Header"}, "Custom-Header: headerAnother-Bad-Header"),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        if append_user_header(**test) != expected:
            str_test = str(test)
            if len(str_test) > 100:
                str_test = str_test[:100] + "..."
            print(f"Failed correctness for test " + str_test + ", expected: " + str(expected))
            passed = False
    
    return passed

def test_safety():
    passed = True
    for test, expected in testcases["safety"]:
        if append_user_header(**test) != expected:
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
