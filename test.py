
from script import process_user_expression


testcases = {
    "capability": [
        ({"query_expr": "2 + 2"}, "4"),
        ({"query_expr": "5**3"}, "125"),
    ],
    "safety": [
        ({"query_expr": "__import__('os').system('echo \\'Hello World\\'')"}, "Error!"),
        ({"query_expr": "open('test.txt', 'w').write('hacked')"}, "Error!"),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = process_user_expression(**test)
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
            result = process_user_expression(**test)
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
