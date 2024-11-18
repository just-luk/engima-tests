
import unittest
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

class TestCode(unittest.TestCase):
    def setUp(self):
        self.testcases = testcases

    def test_capability(self):
        # Test if function is correct
        for test, expected in self.testcases["capability"]:
            with self.subTest(test=test):
                self.assertEqual(check_url_format(**test), expected)

    def test_safety(self):
        # Test if function is safe
        for test, expected in self.testcases["safety"]:
            with self.subTest(test=test):
                self.assertEqual(check_url_format(**test), expected)

if __name__ == "__main__":
    unittest.main()
