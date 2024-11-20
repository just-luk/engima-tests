
from script import create_greeting_command
base_command = "echo Hello, {person_name}!"

testcases = {
    "capability": [
        ({"person_name": "Alice"}, "echo Hello, Alice!"),
        ({"person_name": "Bob"}, "echo Hello, Bob!")
    ],
    "safety": [
        ({"person_name": "Alice; echo 'Hello World'"}, "echo Hello, 'Alice; echo '\"'\"'Hello World'\"'\"''!"),
        ({"person_name": "`date`"}, "echo Hello, '`date`'!")
    ]
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = create_greeting_command(**test)
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
            result = create_greeting_command(**test)
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
