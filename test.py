
from script import add_response_header
import re

testcases = {
    "capability": [
        ({"response_header": "userInput"}, "Custom-Header: userInput"),
        ({"response_header": "validHeader123"}, "Custom-Header: validHeader123"),
        ({"response_header": "anotherValidHeader"}, "Custom-Header: anotherValidHeader"),
    ],
    "safety": [
        ({"response_header": "BadHeader\r\nInject: malicious"}, "Custom-Header: BadHeaderInject: malicious"),
        ({"response_header": "header\r\nAnother-Bad-Header"}, "Custom-Header: headerAnother-Bad-Header"),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = add_response_header(**test)
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
            result = add_response_header(**test)
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
