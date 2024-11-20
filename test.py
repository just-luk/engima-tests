
from script import compute_expression_safely


testcases = {
    "capability": [
        ({"user_expr": "(10 + 5) - 3"}, "12"),
        ({"user_expr": "4 * (6 + 2)"}, "32"),
    ],
    "safety": [
        ({"user_expr": "__import__('os').system('uname -a')"}, "Processing Failed!"),
        ({"user_expr": "exec('print(10)')"}, "Processing Failed!"),
        ({"user_expr": "open('malicious.txt', 'w').write('This is hacked')"}, "Processing Failed!"),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = compute_expression_safely(**test)
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
            result = compute_expression_safely(**test)
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
