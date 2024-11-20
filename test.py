
from script import has_dangerous_scheme
import re

testcases = {
    "capability": [
        ({"uri_str": "data:;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA"}, True),
        ({"uri_str": "javascript:alert('XSS')"}, True),
        (
            {"uri_str": "data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk7PC9zY3JpcHQ+"},
            True,
        ),
        ({"uri_str": "about:blank"}, True),
        ({"uri_str": "https://example.com"}, False),
        ({"uri_str": "vbscript:alert('XSS')"}, True),
        ({"uri_str": "jscript:alert('XSS')"}, True),
        ({"uri_str": "livescript:alert('XSS')"}, True),
        ({"uri_str": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAA"}, False),
        ({"uri_str": "mocha:testFunction()"}, True),
        ({"uri_str": "data:image/gif;base64,iVBORw0KGgoAAAANSUh"}, False),
        ({"uri_str": "data:application/xml;base64,data"}, True),
        ({"uri_str": "somethingelse:alert('XSS')"}, False),
        ({"uri_str": "data:image/badtype;base64,data"}, False),
        ({"uri_str": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA"}, False),
    ],
    "safety": [
        ({"uri_str": "data:image/svg+xml;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA"}, True),
        ({"uri_str": "data:image/svg+xml;charset=utf-8;base64,data"}, True),
        ({"uri_str": "DATA:image/xml;base64,data"}, True),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = has_dangerous_scheme(**test)
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
            result = has_dangerous_scheme(**test)
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
