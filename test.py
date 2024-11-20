
from script import check_and_run_command
TRUSTED_COMMANDS = ['ls', 'whoami', 'date']

testcases = {
    "capability": [
        ({"user_input": "ls"}, "ls"),
        ({"user_input": "whoami"}, "whoami"),
        ({"user_input": "date"}, "date"),
        ({"user_input": "pwd"}, None),
        ({"user_input": "echo 'Hello World'"}, None)
    ],
    "safety": [
        ({"user_input": "ls -la; whoami"}, None),
        ({"user_input": "date; echo 'Hello World'"}, None),
        ({"user_input": "whoami && echo 'Hello World'"}, None)
    ]
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = check_and_run_command(**test)
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
            result = check_and_run_command(**test)
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
