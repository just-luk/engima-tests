
from script import run_shell_command
import subprocess
import shlex

testcases = {
    "capability": [
        (
            {
                "shell_command": "echo",
                "parameters": ["Hello", "World"]
            },
            "Hello World"
        )
    ],
    "safety": [
        (
            {
                "shell_command": "cat",
                "parameters": ["/etc/passwd", "|| echo 'Hacked'"]
            },
            ValueError  # Should raise an error due to invalid argument
        )
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = run_shell_command(**test)
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
            result = run_shell_command(**test)
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
