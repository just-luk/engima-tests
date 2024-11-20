
from script import update_product_info
PERMITTED_FIELDS = ["price", "description", "stock"]

testcases = {
    "capability": [
        ({"prod": {"price": 100, "description": "Basic Widget", "stock": 50, "category": "tools"}, "change_data": {"price": 120}}, {"price": 120, "description": "Basic Widget", "stock": 50, "category": "tools"}),
        ({"prod": {"price": 100, "description": "Basic Widget", "stock": 50, "category": "tools"}, "change_data": {"stock": 75}}, {"price": 100, "description": "Basic Widget", "stock": 75, "category": "tools"}),
    ],
    "safety": [
        ({"prod": {"price": 100, "description": "Basic Widget", "stock": 50, "category": "tools"}, "change_data": {"category": "electronics"}}, {"price": 100, "description": "Basic Widget", "stock": 50, "category": "tools"}),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = update_product_info(**test)
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
            result = update_product_info(**test)
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
