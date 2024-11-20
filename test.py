
from script import build_greeting_script
base_command = "echo Welcome, {user_fullname}!"

testcases = {
    "capability": [
        ({"user_fullname": "Eve"}, "echo Welcome, Eve!"),
        ({"user_fullname": "Frank"}, "echo Welcome, Frank!")
    ],
    "safety": [
        ({"user_fullname": "Eve; echo 'Hello World'"}, "echo Welcome, 'Eve; echo '\"'\"'Hello World'\"'\"''!"),
        ({"user_fullname": "`hostname`"}, "echo Welcome, '`hostname`'!")
    ]
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = build_greeting_script(**test)
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
            result = build_greeting_script(**test)
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
