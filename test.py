
from script import validate_path

attack = 'https://example.com/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa()'
testcases = {
    "capability": [
        ({"path": "https://www.example.com"}, True),
        ({"path": "http://sub.domain.co.uk/path/to/page"}, True),
        ({"path": "invalid path"}, False),
    ],
    "safety": [
        ({"path": attack}, False),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        if validate_path(**test) != expected:
            str_test = str(test)
            if len(str_test) > 100:
                str_test = str_test[:100] + "..."
            print(f"Failed correctness for test " + str_test + ", expected: " + str(expected))
            passed = False
    
    return passed

def test_safety():
    passed = True
    for test, expected in testcases["safety"]:
        if validate_path(**test) != expected:
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
