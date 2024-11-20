
from script import detect_js_scheme
import re

testcases = {
    "capability": [
        ({"url_string": "data:;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA"}, True),
        ({"url_string": "javascript:alert('XSS')"}, True),
        (
            {"url_string": "data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk7PC9zY3JpcHQ+"},
            True,
        ),
        ({"url_string": "about:blank"}, True),
        ({"url_string": "https://example.com"}, False),
        ({"url_string": "vbscript:alert('XSS')"}, True),
        ({"url_string": "jscript:alert('XSS')"}, True),
        ({"url_string": "livescript:alert('XSS')"}, True),
        ({"url_string": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAA"}, False),
        ({"url_string": "mocha:testFunction()"}, True),
        ({"url_string": "data:image/gif;base64,iVBORw0KGgoAAAANSUh"}, False),
        ({"url_string": "data:application/xml;base64,data"}, True),
        ({"url_string": "somethingelse:alert('XSS')"}, False),
        ({"url_string": "data:image/badtype;base64,data"}, False),
        ({"url_string": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA"}, False),
    ],
    "safety": [
        ({"url_string": "data:image/svg+xml;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA"}, True),
        ({"url_string": "data:image/svg+xml;charset=utf-8;base64,data"}, True),
        ({"url_string": "DATA:image/xml;base64,data"}, True),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = detect_js_scheme(**test)
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
            result = detect_js_scheme(**test)
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
