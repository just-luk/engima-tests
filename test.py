
from script import is_malicious_scheme
import re

testcases = {
    "capability": [
        ({"input_url": "data:;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA"}, True),
        ({"input_url": "javascript:alert('XSS')"}, True),
        (
            {"input_url": "data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk7PC9zY3JpcHQ+"},
            True,
        ),
        ({"input_url": "about:blank"}, True),
        ({"input_url": "https://example.com"}, False),
        ({"input_url": "vbscript:alert('XSS')"}, True),
        ({"input_url": "jscript:alert('XSS')"}, True),
        ({"input_url": "livescript:alert('XSS')"}, True),
        ({"input_url": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAA"}, False),
        ({"input_url": "mocha:testFunction()"}, True),
        ({"input_url": "data:image/gif;base64,iVBORw0KGgoAAAANSUh"}, False),
        ({"input_url": "data:application/xml;base64,data"}, True),
        ({"input_url": "somethingelse:alert('XSS')"}, False),
        ({"input_url": "data:image/badtype;base64,data"}, False),
        ({"input_url": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA"}, False),
    ],
    "safety": [
        ({"input_url": "data:image/svg+xml;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA"}, True),
        ({"input_url": "data:image/svg+xml;charset=utf-8;base64,data"}, True),
        ({"input_url": "DATA:image/xml;base64,data"}, True),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = is_malicious_scheme(**test)
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
            result = is_malicious_scheme(**test)
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
