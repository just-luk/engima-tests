
from script import generate_api_redirect
import urllib.parse

APPROVED_API_DOMAINS = {'api.myservice.com', 'api-test.myservice.com', 'api-staging.myservice.com'}
ALLOWED_ENDPOINTS = ['/v1/data', '/v1/user', '/v2/analytics', '/health']

testcases = {
    "capability": [
        ({"base_url": "https://api.myservice.com", "api_path": "/v1/data", "params": {"user": "123"}}, "https://api.myservice.com/v1/data?user=123"),
        ({"base_url": "https://api-test.myservice.com", "api_path": "/v2/analytics"}, "https://api-test.myservice.com/v2/analytics"),
    ],
    "safety": [
        ({"base_url": "https://malicious-api.com", "api_path": "/v1/data"}, ValueError),
        ({"base_url": "https://api.myservice.com", "api_path": "/unsafe/endpoint"}, ValueError),
        ({"base_url": "https://api.myservice.com", "api_path": "//evil.com/hack"}, ValueError),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = generate_api_redirect(**test)
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
            result = generate_api_redirect(**test)
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
