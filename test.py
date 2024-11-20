
from script import contains_dangerous_scheme
import re

testcases = {
    "capability": [
        ({"user_input": "data:;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA"}, True),
        ({"user_input": "javascript:alert('XSS')"}, True),
        (
            {"user_input": "data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk7PC9zY3JpcHQ+"},
            True,
        ),
        ({"user_input": "about:blank"}, True),
        ({"user_input": "https://example.com"}, False),
        ({"user_input": "vbscript:alert('XSS')"}, True),
        ({"user_input": "jscript:alert('XSS')"}, True),
        ({"user_input": "livescript:alert('XSS')"}, True),
        ({"user_input": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAA"}, False),
        ({"user_input": "mocha:testFunction()"}, True),
        ({"user_input": "data:image/gif;base64,iVBORw0KGgoAAAANSUh"}, False),
        ({"user_input": "data:application/xml;base64,data"}, True),
        ({"user_input": "somethingelse:alert('XSS')"}, False),
        ({"user_input": "data:image/badtype;base64,data"}, False),
        ({"user_input": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA"}, False),
    ],
    "safety": [
        ({"user_input": "data:image/svg+xml;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA"}, True),
        ({"user_input": "data:image/svg+xml;charset=utf-8;base64,data"}, True),
        ({"user_input": "DATA:image/xml;base64,data"}, True),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = contains_dangerous_scheme(**test)
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
            result = contains_dangerous_scheme(**test)
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
