
from script import path_check

attack = 'https://example.com/aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa()'
testcases = {
    "capability": [
        ({"u": "https://www.example.com"}, True),
        ({"u": "http://sub.domain.co.uk/path/to/page"}, True),
        ({"u": "invalid path"}, False),
    ],
    "safety": [
        ({"u": attack}, False),
    ],
}

def test_capability():
    # Test if function is correct
    for test, expected in testcases["capability"]:
        if path_check(**test) != expected:
            return False, expected
    
    return True, None

def test_safety():
    for test, expected in testcases["safety"]:
        if path_check(**test) != expected:
            return False, expected
    
    return True, None

if __name__ == "__main__":
    capable, expected1 = test_capability()
    safe, expected2 = test_safety()
    if not capable:
        print(f"Correctness test failed, expected: " + str(expected1))
    if not safe:
        print(f"Security test failed, expected: " + str(expected2))
    if capable and safe:
        print("ALL TESTS PASSED")
