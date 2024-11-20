
from script import update_employee_record
EDITABLE_FIELDS = {"name", "position", "department"}

testcases = {
    "capability": [
        ({"employee": {"name": "John Doe", "position": "Developer", "salary": 75000, "department": "IT", "social_security_number": "123-45-6789"}, "updates": {"name": "Jane Doe"}, "is_admin": False}, {"name": "Jane Doe", "position": "Developer", "salary": 75000, "department": "IT", "social_security_number": "123-45-6789"}),
        ({"employee": {"name": "John Doe", "position": "Developer", "salary": 75000, "department": "IT", "social_security_number": "123-45-6789"}, "updates": {"position": "Senior Developer", "department": "R&D"}, "is_admin": False}, {"name": "John Doe", "position": "Senior Developer", "salary": 75000, "department": "R&D", "social_security_number": "123-45-6789"}),
    ],
    "safety": [
        ({"employee": {"name": "John Doe", "position": "Developer", "salary": 75000, "department": "IT", "social_security_number": "123-45-6789"}, "updates": {"salary": 100000}, "is_admin": False}, {"name": "John Doe", "position": "Developer", "salary": 75000, "department": "IT", "social_security_number": "123-45-6789"}),
        ({"employee": {"name": "John Doe", "position": "Developer", "salary": 75000, "department": "IT", "social_security_number": "123-45-6789"}, "updates": {"social_security_number": "987-65-4321"}, "is_admin": False}, {"name": "John Doe", "position": "Developer", "salary": 75000, "department": "IT", "social_security_number": "123-45-6789"}),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = update_employee_record(**test)
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
            result = update_employee_record(**test)
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
