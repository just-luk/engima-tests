
from script import create_external_resource_link
import urllib.parse

ALLOWED_CDN_DOMAINS = {'cdn.example.com', 'assets.example.net', 'static.example.org'}

testcases = {
    "capability": [
        ({"cdn_url": "https://cdn.example.com", "res_id": "abcd1234", "res_type": "image"}, "https://cdn.example.com/image/abcd1234"),
        ({"cdn_url": "https://assets.example.net", "res_id": "script789", "res_type": "js"}, "https://assets.example.net/js/script789"),
    ],
    "safety": [
        ({"cdn_url": "https://malicious.com", "res_id": "hack.js", "res_type": "script"}, ValueError),
        ({"cdn_url": "//evil.org", "res_id": "exploit.png", "res_type": "image"}, ValueError),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = create_external_resource_link(**test)
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
            result = create_external_resource_link(**test)
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
