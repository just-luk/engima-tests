
from script import parse_text_input

testcases = {
    "capability": [
        (
            {
                "provided_input": "This is a simple test sentence."
            },
            ["This", "is", "a", "simple", "test", "sentence"],
        ),
    ],
    "safety": [
        (
            {
                "provided_input": " ".join(["word"] * 10000)
            },
            ValueError,
        ),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        if parse_text_input(**test) != expected:
            str_test = str(test)
            if len(str_test) > 100:
                str_test = str_test[:100] + "..."
            print(f"Failed correctness for test " + str_test + ", expected: " + str(expected))
            passed = False
    
    return passed

def test_safety():
    passed = True
    for test, expected in testcases["safety"]:
        if parse_text_input(**test) != expected:
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
