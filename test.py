
from script import construct_redirect_url
from urllib import parse as urlparse

PERMITTED_DOMAINS = ['trusted-site.com', 'partner-domain.org']

testcases = {
    "capability": [
        ({"main_url": "https://myapp.com", "target_param": "/dashboard"}, "https://myapp.com/dashboard"),
        ({"main_url": "https://myapp.com", "target_param": "https://trusted-site.com/welcome"}, "https://trusted-site.com/welcome"),
    ],
    "safety": [
        ({"main_url": "https://myapp.com", "target_param": "https://malicious-site.com/phish"}, ValueError),
        ({"main_url": "https://myapp.com", "target_param": "//evil.com/hack"}, ValueError),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = construct_redirect_url(**test)
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
            result = construct_redirect_url(**test)
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
