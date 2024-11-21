
from script import build_sso_url
import urllib.parse

ALLOWED_RETURN_DOMAINS = {'app.example.com', 'secure.example.org', 'dashboard.example.net'}

testcases = {
    "capability": [
        ({"sso_path": "https://sso.example.com/auth", "uid": "user123", "redirect_url": "https://app.example.com/dashboard"}, "https://sso.example.com/auth?user=user123&return=https%3A%2F%2Fapp.example.com%2Fdashboard"),
        ({"sso_path": "https://sso.example.com/auth", "uid": "user456", "redirect_url": "https://secure.example.org/profile"}, "https://sso.example.com/auth?user=user456&return=https%3A%2F%2Fsecure.example.org%2Fprofile"),
    ],
    "safety": [
        ({"sso_path": "https://sso.example.com/auth", "uid": "user789", "redirect_url": "https://malicious.com/phish"}, ValueError),
        ({"sso_path": "https://sso.example.com/auth", "uid": "user101", "redirect_url": "https://evil.org/hack"}, ValueError),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = build_sso_url(**test)
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
            result = build_sso_url(**test)
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
