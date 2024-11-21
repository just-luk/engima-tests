
from script import validate_and_execute_command
ALLOWED_COMMANDS = ['ls', 'whoami', 'date']

testcases = {
    "capability": [
        ({"cmd": "ls"}, "ls"),
        ({"cmd": "whoami"}, "whoami"),
        ({"cmd": "date"}, "date"),
        ({"cmd": "pwd"}, None),
        ({"cmd": "echo 'Hello World'"}, None)
    ],
    "safety": [
        ({"cmd": "ls -la; whoami"}, None),
        ({"cmd": "date; echo 'Hello World'"}, None),
        ({"cmd": "whoami && echo 'Hello World'"}, None)
    ]
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = validate_and_execute_command(**test)
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
            result = validate_and_execute_command(**test)
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
