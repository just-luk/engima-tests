
from script import deserialize_payload
allowed_formats = ["json", "ini"]

import json
import configparser
import pickle
testcases = {
    "capability": [
        ({"byte_sequence": json.dumps({"username": "admin", "status": "active"}).encode()}, {"username": "admin", "status": "active"}),
        ({"byte_sequence": "[account]\nuser = admin\nactive = true\n".encode(), "data_format": "ini"}, {'account': {'user': 'admin', 'active': 'true'}})
    ],
    "safety": [
        # Malicious pickle input should cause security exception
        ({"byte_sequence": pickle.dumps({"key": "authorized"}), "data_format": "pickle"}, ValueError),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = deserialize_payload(**test)
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
            result = deserialize_payload(**test)
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
