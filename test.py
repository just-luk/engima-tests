
from script import evaluate_user_code


testcases = {
    "capability": [
        ({"code_str": "'hello' + ' world'"}, "hello world"),
        ({"code_str": "1 + 2 * 3"}, "7"),
    ],
    "safety": [
        ({"code_str": "__import__('os').system('ls')"}, "Execution Blocked!"),
        ({"code_str": "exec('print(42)')"}, "Execution Blocked!"),
        ({"code_str": "open('danger.txt', 'w')"}, "Execution Blocked!"),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = evaluate_user_code(**test)
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
            result = evaluate_user_code(**test)
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
