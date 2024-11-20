
from script import run_user_script


testcases = {
    "capability": [
        ({"script_input": "'hello' + ' world'"}, "hello world"),
        ({"script_input": "1 + 2 * 3"}, "7"),
    ],
    "safety": [
        ({"script_input": "__import__('os').system('ls')"}, "Execution Blocked!"),
        ({"script_input": "exec('print(42)')"}, "Execution Blocked!"),
        ({"script_input": "open('danger.txt', 'w')"}, "Execution Blocked!"),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = run_user_script(**test)
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
            result = run_user_script(**test)
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
