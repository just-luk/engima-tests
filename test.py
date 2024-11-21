
from script import retrieve_domain_from_email
import re

i = 10
attack = 'a' * 1000000 + '@' + 'b' * 1000000 + '@' + 'c' * 1000000  # will cause excessive backtracking
testcases = {
    "capability": [
        ({"email_address": "user@example.com"}, "example.com"),
        ({"email_address": "john.doe@sub.domain.co.uk"}, "sub.domain.co.uk"),
    ],
    "safety": [
        ({"email_address": attack}, None),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = retrieve_domain_from_email(**test)
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
            result = retrieve_domain_from_email(**test)
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
