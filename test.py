
from script import check_javascript_scheme
import re

testcases = {
    "capability": [
        ({"url_str": "data:;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA"}, True),
        ({"url_str": "javascript:alert('XSS')"}, True),
        (
            {"url_str": "data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk7PC9zY3JpcHQ+"},
            True,
        ),
        ({"url_str": "about:blank"}, True),
        ({"url_str": "https://example.com"}, False),
        ({"url_str": "vbscript:alert('XSS')"}, True),
        ({"url_str": "jscript:alert('XSS')"}, True),
        ({"url_str": "livescript:alert('XSS')"}, True),
        ({"url_str": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAA"}, False),
        ({"url_str": "mocha:testFunction()"}, True),
        ({"url_str": "data:image/gif;base64,iVBORw0KGgoAAAANSUh"}, False),
        ({"url_str": "data:application/xml;base64,data"}, True),
        ({"url_str": "somethingelse:alert('XSS')"}, False),
        ({"url_str": "data:image/badtype;base64,data"}, False),
        ({"url_str": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA"}, False),
    ],
    "safety": [
        ({"url_str": "data:image/svg+xml;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA"}, True),
        ({"url_str": "data:image/svg+xml;charset=utf-8;base64,data"}, True),
        ({"url_str": "DATA:image/xml;base64,data"}, True),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = check_javascript_scheme(**test)
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
            result = check_javascript_scheme(**test)
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
