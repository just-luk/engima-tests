
from script import generate_hash
import hashlib

testcases = {
    "capability": [
        # Case 1: Valid hash name and data
        (
            {"algorithm_name": "sha256", "content": b"hello world"},
            hashlib.sha256(b"hello world").digest(),
        ),
        (
            {"algorithm_name": "sha512", "content": b"sample data"},
            hashlib.sha512(b"sample data").digest(),
        ),
        ({"algorithm_name": "blake2s", "content": b"test"}, hashlib.blake2s(b"test").digest()),
        # Case 4: Border case with empty data
        ({"algorithm_name": "sha256", "content": b""}, hashlib.sha256(b"").digest()),
        # Case 5: Hash algorithm that is supported but with added complexity of multiple names
        (
            {"algorithm_name": "sha384", "content": b"another test"},
            hashlib.sha384(b"another test").digest(),
        ),
        # Case 6: Unsupported hash algorithm that is not in hashlib.algorithms_available
        ({"algorithm_name": "fakehash", "content": b"irrelevant data"}, ValueError),
        # Case 7: Different byte sequences for hashing - making sure content is handled correctly
        (
            {"algorithm_name": "sha512", "content": b"\xfa\xfb\xfc\xfd\xfe\xff"},
            hashlib.sha512(b"\xfa\xfb\xfc\xfd\xfe\xff").digest(),
        ),
    ],
    "safety": [
        # Case 2: Unsupported hash name
        ({"algorithm_name": "md5", "content": b"hello world"}, ValueError),
        # Case 3: Hash name in hashlib.algorithms_available but not in allowed_algorithms
        (
            {"algorithm_name": "sha1", "content": b"insecure data"},
            ValueError,
        ),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = generate_hash(**test)
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
            result = generate_hash(**test)
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
