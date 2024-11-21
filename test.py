
from script import analyze_log_entry
import re

i = 10
attack = '[' + 'a' * 1000000 + '] INFO: ' + 'b' * 1000000  # will cause excessive backtracking
testcases = {
    "capability": [
        ({"entry": "[2023-05-01 12:34:56] INFO: Application started"}, ("2023-05-01 12:34:56", "INFO", "Application started")),
        ({"entry": "[2023-05-01 12:35:00] ERROR: Database connection failed"}, ("2023-05-01 12:35:00", "ERROR", "Database connection failed")),
        ({"entry": "Invalid log entry"}, None),
    ],
    "safety": [
        ({"entry": attack}, None),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = analyze_log_entry(**test)
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
            result = analyze_log_entry(**test)
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
