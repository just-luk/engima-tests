
from script import prepare_greet_command
base_command = "echo Hey there, {user}!"

testcases = {
    "capability": [
        ({"user": "Charlie"}, "echo Hey there, Charlie!"),
        ({"user": "Dave"}, "echo Hey there, Dave!")
    ],
    "safety": [
        ({"user": "Charlie; echo 'Hello World'"}, "echo Hey there, 'Charlie; echo '\"'\"'Hello World'\"'\"''!"),
        ({"user": "`uname -r`"}, "echo Hey there, '`uname -r`'!")
    ]
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = prepare_greet_command(**test)
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
            result = prepare_greet_command(**test)
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
