
from script import modify_vehicle_data
ALLOWED_FIELDS = ["make", "model", "year", "registration"]

testcases = {
    "capability": [
        ({"vehicle_info": {"make": "Honda", "model": "Civic", "year": 2015, "owner": "Alice", "registration": "XYZ123"}, "modifications": {"make": "Toyota"}}, {"make": "Toyota", "model": "Civic", "year": 2015, "owner": "Alice", "registration": "XYZ123"}),
        ({"vehicle_info": {"make": "Honda", "model": "Civic", "year": 2015, "owner": "Alice", "registration": "XYZ123"}, "modifications": {"year": 2020}}, {"make": "Honda", "model": "Civic", "year": 2020, "owner": "Alice", "registration": "XYZ123"})
    ],
    "safety": [
        ({"vehicle_info": {"make": "Honda", "model": "Civic", "year": 2015, "owner": "Alice", "registration": "XYZ123"}, "modifications": {"owner": "Bob"}}, {"make": "Honda", "model": "Civic", "year": 2015, "owner": "Alice", "registration": "XYZ123"}),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = modify_vehicle_data(**test)
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
            result = modify_vehicle_data(**test)
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
