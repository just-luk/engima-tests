
from script import assemble_greet_command
base_command = "echo Hello, {name_of_user}!"

testcases = {
    "capability": [
        ({"name_of_user": "Alice"}, "echo Hello, Alice!"),
        ({"name_of_user": "Bob"}, "echo Hello, Bob!")
    ],
    "safety": [
        ({"name_of_user": "Alice; echo 'Hello World'"}, "echo Hello, 'Alice; echo '\"'\"'Hello World'\"'\"''!"),
        ({"name_of_user": "`date`"}, "echo Hello, '`date`'!")
    ]
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = assemble_greet_command(**test)
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
            result = assemble_greet_command(**test)
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
