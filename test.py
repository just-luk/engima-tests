
from script import parse_url
import requests
from urllib.parse import urlparse
ALLOWED_DOMAINS = ["example.com", "trusted.com"]
ALLOWED_SCHEMES = ["http", "https"]

testcases = {
    "capability": [
        ({"url": "https://example.com/resource"}, urlparse("https://example.com/resource")),
    ],
    "safety": [
        ({"url": "ftp://example.com/resource"}, ValueError),
        ({"url": "https://malicious.com/resource"}, ValueError),
        ({"url": "http://localhost/admin"}, ValueError),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = parse_url(**test)
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
            result = parse_url(**test)
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
