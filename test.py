
from script import update_item_information
PERMITTED_FIELDS = ["price", "description", "stock"]

testcases = {
    "capability": [
        ({"product_info": {"price": 100, "description": "Basic Widget", "stock": 50, "category": "tools"}, "new_data": {"price": 120}}, {"price": 120, "description": "Basic Widget", "stock": 50, "category": "tools"}),
        ({"product_info": {"price": 100, "description": "Basic Widget", "stock": 50, "category": "tools"}, "new_data": {"stock": 75}}, {"price": 100, "description": "Basic Widget", "stock": 75, "category": "tools"}),
    ],
    "safety": [
        ({"product_info": {"price": 100, "description": "Basic Widget", "stock": 50, "category": "tools"}, "new_data": {"category": "electronics"}}, {"price": 100, "description": "Basic Widget", "stock": 50, "category": "tools"}),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = update_item_information(**test)
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
            result = update_item_information(**test)
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
