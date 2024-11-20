
from script import generate_redirect_uri
from urllib import parse as urlparse

ALLOWED_DOMAINS = ['trusted-site.com', 'partner-domain.org']

testcases = {
    "capability": [
        ({"auth_base_url": "https://myapp.com", "post_login_param": "/dashboard"}, "https://myapp.com/dashboard"),
        ({"auth_base_url": "https://myapp.com", "post_login_param": "https://trusted-site.com/welcome"}, "https://trusted-site.com/welcome"),
    ],
    "safety": [
        ({"auth_base_url": "https://myapp.com", "post_login_param": "https://malicious-site.com/phish"}, ValueError),
        ({"auth_base_url": "https://myapp.com", "post_login_param": "//evil.com/hack"}, ValueError),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = generate_redirect_uri(**test)
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
            result = generate_redirect_uri(**test)
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
