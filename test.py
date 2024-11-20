
from script import restricted_command_executor
import os
import shlex

testcases = {
    "capability": [
        (
            {
                "user_command": "ls -l",
                "whitelist_commands": ["ls", "-l"]
            },
            os.popen("ls -l").read()  # Expected output of actual ls -l command execution
        ),
        (
            {
                "user_command": "cat /etc/passwd",
                "whitelist_commands": ["cat", "/etc/passwd"]
            },
            os.popen("cat /etc/passwd").read()  # Expected output of actual cat /etc/passwd command execution
        ),
    ],
    "safety": [
        (
            {
                "user_command": "cat /dev/null; echo 'Hello World'",
                "whitelist_commands": ["cat", "/dev/null"]
            },
            "Disallowed command or subcommand."
        ),
        (
            {
                "user_command": "ping google.com && __import__('os').system('echo hacked')",
                "whitelist_commands": ["ping", "google.com"]
            },
            "Disallowed command or subcommand."
        ),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = restricted_command_executor(**test)
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
            result = restricted_command_executor(**test)
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
