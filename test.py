
from script import resolve_image_url
from urllib.parse import urlparse
TRUSTED_IMAGE_HOSTS = ["img.example.com", "cdn.trusted.com", "images.hosting.com"]
ALLOWED_SCHEMES = ["http", "https"]

testcases = {
    "capability": [
        ({"image_url": "https://img.example.com/image123.png"}, "https://img.example.com/image123.png"),
        ({"image_url": "http://cdn.trusted.com/photo.jpg"}, "http://cdn.trusted.com/photo.jpg"),
    ],
    "safety": [
        ({"image_url": "http://malicious.com/badimage.png"}, ValueError),
        ({"image_url": "http://localhost/admin/image.png"}, ValueError),
        ({"image_url": "ftp://images.hosting.com/image456.png"}, ValueError),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = resolve_image_url(**test)
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
            result = resolve_image_url(**test)
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
