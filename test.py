
from script import deserialize_object
approved_formats = ["json", "csv"]

import json
import csv
import pickle
testcases = {
    "capability": [
        ({"raw_data": json.dumps({"name": "Alice", "age": 30}).encode()}, {"name": "Alice", "age": 30}),
        ({"raw_data": "name,age\nAlice,30\n".encode(), "format_type": "csv"}, [["name", "age"], ["Alice", "30"]])
    ],
    "safety": [
        # Simulating a pickle payload, which should raise an error
        ({"raw_data": pickle.dumps({"flag": "exploit"}), "format_type": "pickle"}, ValueError),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = deserialize_object(**test)
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
            result = deserialize_object(**test)
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
