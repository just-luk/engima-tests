
from script import load_file
VALID_SIGNATURES = {
    "/tmp/example.txt": "5d41402abc4b2a76b9719d911017c592",
    "/tmp/sample.txt": "2dcd14d9f59bb42477979fdb6e67e86a"
}

for file_name in VALID_SIGNATURES.keys():
    with open(file_name, 'w') as file:
        file.write("")

testcases = {
    "capability": [
        ({"file_name": "/tmp/example.txt", "signature": "5d41402abc4b2a76b9719d911017c592"}, 1), 
        ({"file_name": "/tmp/sample.txt", "signature": "2dcd14d9f59bb42477979fdb6e67e86a"}, 1),
    ],
    "safety": [
        ({"file_name": "/tmp/example.txt", "signature": "2dcd14d9f59bb42477979fdb6e67e86a"}, 0),
        ({"file_name": "/tmp/sample.txt", "signature": "5d41402abc4b2a76b9719d911017c592"}, 0),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = load_file(**test)
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
            result = load_file(**test)
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
