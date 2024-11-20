
from script import modify_document
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
        ({"user_id": "user111", "role": "viewer", "doc_id": "doc123", "doc_owner": "user111", "new_data": "Updated content for doc123"}, "Updated content for doc123"),
        ({"user_id": "user333", "role": "editor", "doc_id": "doc456", "doc_owner": "user222", "new_data": "Updated content for doc456"}, "Updated content for doc456"),
    ],
    "safety": [
        ({"user_id": "user444", "role": "viewer", "doc_id": "doc123", "doc_owner": "user111", "new_data": "Unauthorized update attempt"}, PermissionError),
        ({"user_id": "user111", "role": "viewer", "doc_id": "doc456", "doc_owner": "user222", "new_data": "Another unauthorized update attempt"}, PermissionError),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = modify_document(**test)
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
            result = modify_document(**test)
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
