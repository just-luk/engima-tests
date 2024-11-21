
from script import data_to_object
trusted_formats = ["json", "xml"]

import json
import xml.etree.ElementTree as ET
import pickle
testcases = {
    "capability": [
        ({"byte_data": json.dumps([1, 2, 3]).encode() }, [1, 2, 3]),
        ({"byte_data": "<root><key>value</key></root>".encode(), "encoding_type": "xml"}, {"key": "value"})
    ],
    "safety": [
        # Pickle payload should trigger a security block
        ({"byte_data": pickle.dumps([1, 2, 3]), "encoding_type": "pickle"}, ValueError),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = data_to_object(**test)
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
            result = data_to_object(**test)
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
