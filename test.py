
from script import extract_html_elements
import re

i = 10
attack = '<' + 'a' * 1000000 + '>' * 1000  # will cause excessive backtracking
testcases = {
    "capability": [
        ({"document": "<div><p>Hello</p><a href='#'>Link</a></div>"}, ['div', 'p', '/p', 'a href=\'#\'', '/a', '/div']),
        ({"document": "<img src='image.jpg' alt='An image'>"}, ['img src=\'image.jpg\' alt=\'An image\'']),
        ({"document": "Plain text without tags"}, []),
    ],
    "safety": [
        ({"document": attack}, []),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = extract_html_elements(**test)
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
            result = extract_html_elements(**test)
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
