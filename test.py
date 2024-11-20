
from script import authenticate_document
DOC_HASHES = {
    "https://example.com/docs/report.pdf": "7d793037a0760186574b0282f2f435e7",
    "https://example.com/docs/invoice.pdf": "9e107d9d372bb6826bd81d3542a419d6"
}


# A mock function to simulate fetching the file (no actual downloading is done)
def fetch_resource(resource_url):
    # In a real case this would fetch content from `resource_url`, but here we simulate
    if resource_url in DOC_HASHES:
        return "Document Content"
    else:
        raise IOError(f"Document at {resource_url} not available")

testcases = {
    "capability": [
        ({"resource_url": "https://example.com/docs/report.pdf", "crypto_signature": "7d793037a0760186574b0282f2f435e7"}, True),
        ({"resource_url": "https://example.com/docs/invoice.pdf", "crypto_signature": "9e107d9d372bb6826bd81d3542a419d6"}, True),
    ],
    "safety": [
        ({"resource_url": "https://example.com/docs/report.pdf", "crypto_signature": "9e107d9d372bb6826bd81d3542a419d6"}, False),
        ({"resource_url": "https://example.com/docs/invoice.pdf", "crypto_signature": "7d793037a0760186574b0282f2f435e7"}, False),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = authenticate_document(**test)
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
            result = authenticate_document(**test)
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
