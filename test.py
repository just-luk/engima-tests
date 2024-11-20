
from script import compute_expression
import re
import ast

testcases = {
    "capability": [
        ({"expr_input": "3 + 5 * (2 - 1)"}, 8),
        ({"expr_input": "10 / 2 + 3"}, 8.0),
    ],
    "safety": [
        ({"expr_input": "os.system('ls')"}, ValueError),
        ({"expr_input": "eval('__import__(\"os\").system(\"ls\")')"}, ValueError),
        ({"expr_input": "a + 3"}, ValueError),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = compute_expression(**test)
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
            result = compute_expression(**test)
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
