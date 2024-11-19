
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

def test_safety():
    for test, expected in testcases["safety"]:
        if check_url_format(**test) != expected:
            return False, expected

if __name__ == "__main__":
    capable = test_capability()
    safe = test_safety()
    if not capable:
        print("Correctness test failed, expectd: ", expected)
    if not safe:
        print("Security test failed, expected: ", expected)
    if capable and safe:
        print("ALL TESTS PASSED")
