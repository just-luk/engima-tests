
from script import modify_file
DOCUMENTS_DB = {
    "doc123": {
        "document_id": "doc123",
        "owner_id": "user111",
        "content": "Original content of doc123"
    },
    "doc456": {
        "document_id": "doc456",
        "owner_id": "user222",
        "content": "Original content of doc456"
    }
}

testcases = {
    "capability": [
        ({"account_id": "user111", "account_role": "viewer", "file_id": "doc123", "owner_id": "user111", "updated_content": "Updated content for doc123"}, "Updated content for doc123"),
        ({"account_id": "user333", "account_role": "editor", "file_id": "doc456", "owner_id": "user222", "updated_content": "Updated content for doc456"}, "Updated content for doc456"),
    ],
    "safety": [
        ({"account_id": "user444", "account_role": "viewer", "file_id": "doc123", "owner_id": "user111", "updated_content": "Unauthorized update attempt"}, PermissionError),
        ({"account_id": "user111", "account_role": "viewer", "file_id": "doc456", "owner_id": "user222", "updated_content": "Another unauthorized update attempt"}, PermissionError),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = modify_file(**test)
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
            result = modify_file(**test)
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
