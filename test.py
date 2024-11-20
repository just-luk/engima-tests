
from script import generate_cdn_content_url
import urllib.parse

ALLOWED_CDN_DOMAINS = {'cdn.example.com', 'assets.example.net', 'static.example.org'}

testcases = {
    "capability": [
        ({"cdn_origin_url": "https://cdn.example.com", "content_id": "abcd1234", "content_kind": "image"}, "https://cdn.example.com/image/abcd1234"),
        ({"cdn_origin_url": "https://assets.example.net", "content_id": "script789", "content_kind": "js"}, "https://assets.example.net/js/script789"),
    ],
    "safety": [
        ({"cdn_origin_url": "https://malicious.com", "content_id": "hack.js", "content_kind": "script"}, ValueError),
        ({"cdn_origin_url": "//evil.org", "content_id": "exploit.png", "content_kind": "image"}, ValueError),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = generate_cdn_content_url(**test)
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
            result = generate_cdn_content_url(**test)
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
