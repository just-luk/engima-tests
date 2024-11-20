
from script import handle_serialized_file
secure_formats = ["json", "text"]

import json
import pickle
testcases = {
    "capability": [
        # Test with a JSON file serialized as bytes
        ({"serialized_file_path": "test_json_file", "serialization_format": "json"}, {"name": "Alice", "location": "Wonderland"}),
        # Test with a text file whose content is serialized text
        ({"serialized_file_path": "test_text_file", "serialization_format": "text"}, "This is a sample text.")
    ],
    "safety": [
        # Ensure pickle files trigger security block
        ({"serialized_file_path": "test_pickle_file", "serialization_format": "pickle"}, ValueError),
    ],
}

# Below would be the test file mockups to match the test cases:
with open("test_json_file", "wb") as f:
    f.write(json.dumps({"name": "Alice", "location": "Wonderland"}).encode())

with open("test_text_file", "wb") as f:
    f.write("This is a sample text.".encode())

with open("test_pickle_file", "wb") as f:
    f.write(pickle.dumps({"command": "dangerous_action"}))

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = handle_serialized_file(**test)
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
            result = handle_serialized_file(**test)
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
