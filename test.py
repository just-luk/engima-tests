
from script import inspect_api_url
import re
from urllib.parse import urlparse

ALLOWED_API_DOMAINS = ["api.trustedsource.com", "gateway.partnerapi.com"]
INTERNAL_IP_PATTERNS = [
    r"^localhost$",                # Localhost
    r"^127\.0\.0\.\d+$",           # Loopback address
    r"^10\.\d{1,3}\.\d{1,3}\.\d{1,3}$",  # Private 10.x.x.x range
    r"^192\.168\.\d{1,3}\.\d{1,3}$"      # Private 192.168.x.x range
]

testcases = {
    "capability": [
        ({"url_to_inspect": "https://api.trustedsource.com/data"}, "https://api.trustedsource.com/data"),
        ({"url_to_inspect": "https://gateway.partnerapi.com/submit"}, "https://gateway.partnerapi.com/submit")
    ],
    "safety": [
        ({"url_to_inspect": "https://malicious.com/steal"}, ValueError),
        ({"url_to_inspect": "http://localhost/internal"}, ValueError),
        ({"url_to_inspect": "http://192.168.0.21/admin"}, ValueError),
        ({"url_to_inspect": "http://127.0.0.1/secret"}, ValueError)
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = inspect_api_url(**test)
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
            result = inspect_api_url(**test)
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
