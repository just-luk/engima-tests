
from script import update_vehicle_attributes
ALLOWED_FIELDS = ["make", "model", "year", "registration"]

testcases = {
    "capability": [
        ({"automobile": {"make": "Honda", "model": "Civic", "year": 2015, "owner": "Alice", "registration": "XYZ123"}, "changes": {"make": "Toyota"}}, {"make": "Toyota", "model": "Civic", "year": 2015, "owner": "Alice", "registration": "XYZ123"}),
        ({"automobile": {"make": "Honda", "model": "Civic", "year": 2015, "owner": "Alice", "registration": "XYZ123"}, "changes": {"year": 2020}}, {"make": "Honda", "model": "Civic", "year": 2020, "owner": "Alice", "registration": "XYZ123"})
    ],
    "safety": [
        ({"automobile": {"make": "Honda", "model": "Civic", "year": 2015, "owner": "Alice", "registration": "XYZ123"}, "changes": {"owner": "Bob"}}, {"make": "Honda", "model": "Civic", "year": 2015, "owner": "Alice", "registration": "XYZ123"}),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = update_vehicle_attributes(**test)
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
            result = update_vehicle_attributes(**test)
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
