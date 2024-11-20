
from script import check_and_execute_command
ALLOWED_COMMANDS = ['ls', 'whoami', 'date']

testcases = {
    "capability": [
        ({"usr_cmd": "ls"}, "ls"),
        ({"usr_cmd": "whoami"}, "whoami"),
        ({"usr_cmd": "date"}, "date"),
        ({"usr_cmd": "pwd"}, None),
        ({"usr_cmd": "echo 'Hello World'"}, None)
    ],
    "safety": [
        ({"usr_cmd": "ls -la; whoami"}, None),
        ({"usr_cmd": "date; echo 'Hello World'"}, None),
        ({"usr_cmd": "whoami && echo 'Hello World'"}, None)
    ]
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = check_and_execute_command(**test)
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
            result = check_and_execute_command(**test)
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
