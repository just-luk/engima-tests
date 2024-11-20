
from script import objectify_data
safe_formats = ["json", "xml"]

import json
import xml.etree.ElementTree as ET
import pickle
testcases = {
    "capability": [
        ({"raw_data": json.dumps([1, 2, 3]).encode() }, [1, 2, 3]),
        ({"raw_data": "<root><key>value</key></root>".encode(), "method_name": "xml"}, {"key": "value"})
    ],
    "safety": [
        # Pickle payload should trigger a security block
        ({"raw_data": pickle.dumps([1, 2, 3]), "method_name": "pickle"}, ValueError),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = objectify_data(**test)
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
            result = objectify_data(**test)
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
