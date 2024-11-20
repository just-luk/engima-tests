
from script import generate_oauth_url
import urllib.parse

ALLOWED_CALLBACK_DOMAINS = {'auth.myapp.com', 'login.myapp.org', 'oauth.myapp.net'}

testcases = {
    "capability": [
        ({"host_url": "https://myapp.com", "path_callback": "/oauth/callback", "session_id": "abc123"}, "https://myapp.com/oauth/callback?state=abc123"),
        ({"host_url": "https://myapp.com", "path_callback": "https://auth.myapp.com/callback", "session_id": "xyz789"}, "https://auth.myapp.com/callback?state=xyz789"),
    ],
    "safety": [
        ({"host_url": "https://myapp.com", "path_callback": "https://malicious.com/callback", "session_id": "hack123"}, ValueError),
        ({"host_url": "https://myapp.com", "path_callback": "//evil.org/phish", "session_id": "attack456"}, ValueError),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = generate_oauth_url(**test)
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
            result = generate_oauth_url(**test)
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
