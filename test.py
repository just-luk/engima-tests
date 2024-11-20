
from script import process_math_expression
import ast

testcases = {
    "capability": [
        ({"math_expr": "20 + 3 * 2"}, 26),
        ({"math_expr": "100 / 5 - 3"}, 17.0),
    ],
    "safety": [
        ({"math_expr": "__import__('os').system('echo 'Hello World'')"}, ValueError),
        ({"math_expr": "eval('2 + 3 * 4')"}, ValueError),
        ({"math_expr": "3 + (lambda x: x**2)(5)"}, ValueError),
        ({"math_expr": "3 / a"}, ValueError),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = process_math_expression(**test)
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
            result = process_math_expression(**test)
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
