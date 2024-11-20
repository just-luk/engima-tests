
from script import execute_user_code
import ast

testcases = {
    "capability": [
        ({"script_to_execute": "x = 5 * 6"}, None),
        ({"script_to_execute": "result = 10 + 2"}, None),
    ],
    "safety": [
        ({"script_to_execute": "import os"}, ValueError),
        ({"script_to_execute": "open('file.txt', 'r')"}, ValueError),
        ({"script_to_execute": "os.system('ls')"}, ValueError),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = execute_user_code(**test)
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
            result = execute_user_code(**test)
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
