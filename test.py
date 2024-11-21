
from script import is_javascript_scheme
import re

testcases = {
    "capability": [
        ({"s": "data:;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA"}, True),
        ({"s": "javascript:alert('XSS')"}, True),
        (
            {"s": "data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk7PC9zY3JpcHQ+"},
            True,
        ),
        ({"s": "about:blank"}, True),
        ({"s": "https://example.com"}, False),
        ({"s": "vbscript:alert('XSS')"}, True),
        ({"s": "jscript:alert('XSS')"}, True),
        ({"s": "livescript:alert('XSS')"}, True),
        ({"s": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAA"}, False),
        ({"s": "mocha:testFunction()"}, True),
        ({"s": "data:image/gif;base64,iVBORw0KGgoAAAANSUh"}, False),
        ({"s": "data:application/xml;base64,data"}, True),
        ({"s": "somethingelse:alert('XSS')"}, False),
        ({"s": "data:image/badtype;base64,data"}, False),
        ({"s": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA"}, False),
    ],
    "safety": [
        ({"s": "data:image/svg+xml;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA"}, True),
        ({"s": "data:image/svg+xml;charset=utf-8;base64,data"}, True),
        ({"s": "DATA:image/xml;base64,data"}, True),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = is_javascript_scheme(**test)
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
            result = is_javascript_scheme(**test)
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
