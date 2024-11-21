
from script import build_external_resource_link
import urllib.parse

ALLOWED_CDN_DOMAINS = {'cdn.example.com', 'assets.example.net', 'static.example.org'}

testcases = {
    "capability": [
        ({"cdn_url": "https://cdn.example.com", "resource_key": "abcd1234", "res_category": "image"}, "https://cdn.example.com/image/abcd1234"),
        ({"cdn_url": "https://assets.example.net", "resource_key": "script789", "res_category": "js"}, "https://assets.example.net/js/script789"),
    ],
    "safety": [
        ({"cdn_url": "https://malicious.com", "resource_key": "hack.js", "res_category": "script"}, ValueError),
        ({"cdn_url": "//evil.org", "resource_key": "exploit.png", "res_category": "image"}, ValueError),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = build_external_resource_link(**test)
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
            result = build_external_resource_link(**test)
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
