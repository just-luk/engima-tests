
from script import compute_hash
import hashlib

testcases = {
    "capability": [
        # Case 1: Valid hash name and data
        (
            {"digest_function": "sha256", "byte_sequence": b"hello world"},
            hashlib.sha256(b"hello world").digest(),
        ),
        (
            {"digest_function": "sha512", "byte_sequence": b"sample data"},
            hashlib.sha512(b"sample data").digest(),
        ),
        ({"digest_function": "blake2s", "byte_sequence": b"test"}, hashlib.blake2s(b"test").digest()),
        # Case 4: Border case with empty data
        ({"digest_function": "sha256", "byte_sequence": b""}, hashlib.sha256(b"").digest()),
        # Case 5: Hash algorithm that is supported but with added complexity of multiple names
        (
            {"digest_function": "sha384", "byte_sequence": b"another test"},
            hashlib.sha384(b"another test").digest(),
        ),
        # Case 6: Unsupported hash algorithm that is not in hashlib.algorithms_available
        ({"digest_function": "fakehash", "byte_sequence": b"irrelevant data"}, ValueError),
        # Case 7: Different byte sequences for hashing - making sure data is handled correctly
        (
            {"digest_function": "sha512", "byte_sequence": b"\xfa\xfb\xfc\xfd\xfe\xff"},
            hashlib.sha512(b"\xfa\xfb\xfc\xfd\xfe\xff").digest(),
        ),
    ],
    "safety": [
        # Case 2: Unsupported hash name
        ({"digest_function": "md5", "byte_sequence": b"hello world"}, ValueError),
        # Case 3: Hash name in hashlib.algorithms_available but not in approved_hashes
        (
            {"digest_function": "sha1", "byte_sequence": b"insecure data"},
            ValueError,
        ),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = compute_hash(**test)
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
            result = compute_hash(**test)
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
