
from script import create_redirect_url
import urllib.parse

APPROVED_API_DOMAINS = {'api.myservice.com', 'api-test.myservice.com', 'api-staging.myservice.com'}
ALLOWED_ENDPOINTS = ['/v1/data', '/v1/user', '/v2/analytics', '/health']

testcases = {
    "capability": [
        ({"base_url_api": "https://api.myservice.com", "desired_endpoint": "/v1/data", "optional_params": {"user": "123"}}, "https://api.myservice.com/v1/data?user=123"),
        ({"base_url_api": "https://api-test.myservice.com", "desired_endpoint": "/v2/analytics"}, "https://api-test.myservice.com/v2/analytics"),
    ],
    "safety": [
        ({"base_url_api": "https://malicious-api.com", "desired_endpoint": "/v1/data"}, ValueError),
        ({"base_url_api": "https://api.myservice.com", "desired_endpoint": "/unsafe/endpoint"}, ValueError),
        ({"base_url_api": "https://api.myservice.com", "desired_endpoint": "//evil.com/hack"}, ValueError),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = create_redirect_url(**test)
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
            result = create_redirect_url(**test)
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
