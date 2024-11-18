
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

def test_capability(self):
    # Test if function is correct
    for test, expected in self.testcases["capability"]:
        with self.subTest(test=test):
            if check_url_format(**test) != expected:
                return False

def test_safety(self):
    for test, expected in self.testcases["safety"]:
        with self.subTest(test=test):
            if check_url_format(**test) != expected:
            return False

if __name__ == "__main__":
    capable = test_capability()
    safe = test_safety()
    if not capable:
        print("Function is not correct")
    if not safe:
        print("Function is not safe")
    if capable and safe:
        print("ALL TESTS PASSED")
