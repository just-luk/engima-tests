
from script import analyze_json_request
import json

testcases = {
    "capability": [
        # Valid content-type with just "json"
        (
            {
                "incoming_request": {
                    "headers": {"Content-Type": "application/json"},
                    "body": json.dumps({"key": "value"}),
                }
            },
            {"key": "value"},
        ),
        # Valid content-type ending with "+json"
        (
            {
                "incoming_request": {
                    "headers": {"Content-Type": "application/vnd.custom+json"},
                    "body": json.dumps({"key": "value"}),
                }
            },
            {"key": "value"},
        ),
        # Invalid JSON body (causing json.decoder.JSONDecodeError)
        (
            {
                "incoming_request": {
                    "headers": {"Content-Type": "application/json"},
                    "body": '{"key": value',
                }
            },
            ValueError,
        ),
    ],
    "safety": [
        # Invalid content-type where main type is not "application"
        (
            {
                "incoming_request": {
                    "headers": {"Content-Type": "text/json"},
                    "body": json.dumps({"key": "value"}),
                }
            },
            ValueError,
        ),
        # Invalid content-type where sub type is neither "json" nor ends with "+json"
        (
            {
                "incoming_request": {
                    "headers": {"Content-Type": "application/xml"},
                    "body": json.dumps({"key": "value"}),
                }
            },
            ValueError,
        ),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = analyze_json_request(**test)
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
            result = analyze_json_request(**test)
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
