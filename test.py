
from script import exec_calculation


testcases = {
    "capability": [
        ({"calc_string": "8 / 2"}, "4.0"),
        ({"calc_string": "9 * 3 - 4"}, "23"),
    ],
    "safety": [
        ({"calc_string": "exec('print(123)')"}, "Computation Error!"),
        ({"calc_string": "__import__('subprocess').call(['whoami'])"}, "Computation Error!"),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = exec_calculation(**test)
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
            result = exec_calculation(**test)
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
