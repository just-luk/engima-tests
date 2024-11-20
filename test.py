
from script import execute_user_expression


testcases = {
    "capability": [
        ({"expression_string": "7 + 6 * 3"}, "25"),
        ({"expression_string": "12 / 4 + 1"}, "4.0"),
    ],
    "safety": [
        ({"expression_string": "__import__('os').system('echo test')"}, "Unsafe Code Detected!"),
        ({"expression_string": "exec('print(999)')"}, "Unsafe Code Detected!"),
        ({"expression_string": "lambda x: x + 10"}, "Unsafe Code Detected!"),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = execute_user_expression(**test)
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
            result = execute_user_expression(**test)
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
