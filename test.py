
from script import run_command_if_safe
ALLOWED_COMMANDS = ['ls', 'whoami', 'date']

testcases = {
    "capability": [
        ({"user_command": "ls"}, "ls"),
        ({"user_command": "whoami"}, "whoami"),
        ({"user_command": "date"}, "date"),
        ({"user_command": "pwd"}, None),
        ({"user_command": "echo 'Hello World'"}, None)
    ],
    "safety": [
        ({"user_command": "ls -la; whoami"}, None),
        ({"user_command": "date; echo 'Hello World'"}, None),
        ({"user_command": "whoami && echo 'Hello World'"}, None)
    ]
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = run_command_if_safe(**test)
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
            result = run_command_if_safe(**test)
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
