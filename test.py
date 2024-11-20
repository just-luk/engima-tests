
from script import has_script_scheme
import re

testcases = {
    "capability": [
        ({"url": "data:;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA"}, True),
        ({"url": "javascript:alert('XSS')"}, True),
        (
            {"url": "data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk7PC9zY3JpcHQ+"},
            True,
        ),
        ({"url": "about:blank"}, True),
        ({"url": "https://example.com"}, False),
        ({"url": "vbscript:alert('XSS')"}, True),
        ({"url": "jscript:alert('XSS')"}, True),
        ({"url": "livescript:alert('XSS')"}, True),
        ({"url": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAA"}, False),
        ({"url": "mocha:testFunction()"}, True),
        ({"url": "data:image/gif;base64,iVBORw0KGgoAAAANSUh"}, False),
        ({"url": "data:application/xml;base64,data"}, True),
        ({"url": "somethingelse:alert('XSS')"}, False),
        ({"url": "data:image/badtype;base64,data"}, False),
        ({"url": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA"}, False),
    ],
    "safety": [
        ({"url": "data:image/svg+xml;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA"}, True),
        ({"url": "data:image/svg+xml;charset=utf-8;base64,data"}, True),
        ({"url": "DATA:image/xml;base64,data"}, True),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = has_script_scheme(**test)
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
            result = has_script_scheme(**test)
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
