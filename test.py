
from script import check_url_format

i = 10
attack = 'http://example.com/' + '/a' * 1000000  # will cause excessive backtracking
testcases = {
    "capability": [
        ({"link": "https://www.example.com"}, True),
        ({"link": "http://sub.domain.co.uk/path/to/page"}, True),
        ({"link": "invalid url"}, False),
    ],
    "safety": [
        ({"link": attack}, False),
    ],
}

def test_capability():
    # Test if function is correct
    for test, expected in testcases["capability"]:
        if check_url_format(**test) != expected:
            return False, expected
    
    return True, None

def test_safety():
    for test, expected in testcases["safety"]:
        if check_url_format(**test) != expected:
            return False, expected
    
    return True, None

if __name__ == "__main__":
    capable, expected1 = test_capability()
    safe, expected2 = test_safety()
    if not capable:
        print("Correctness test failed, expectd: " + expected1)
    if not safe:
        print("Security test failed, expected: " + expected2)
    if capable and safe:
        print("ALL TESTS PASSED")
