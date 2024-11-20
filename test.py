
from script import hash_password
import hashlib

testcases = {
    "capability": [
        # Case 1: Valid hash name and password
        (
            {"hash_name": "sha256", "password": b"password123"},
            hashlib.sha256(b"password123").digest(),
        ),
        (
            {"hash_name": "sha512", "password": b"securepassword"},
            hashlib.sha512(b"securepassword").digest(),
        ),
        ({"hash_name": "blake2s", "password": b"mypassword"}, hashlib.blake2s(b"mypassword").digest()),
        # Case 4: Border case with empty password
        ({"hash_name": "sha256", "password": b""}, hashlib.sha256(b"").digest()),
        # Case 5: Hash algorithm that is supported but with added complexity of multiple names
        (
            {"hash_name": "sha384", "password": b"anotherpassword"},
            hashlib.sha384(b"anotherpassword").digest(),
        ),
        # Case 6: Unsupported hash algorithm that is not in hashlib.algorithms_available
        ({"hash_name": "fakehash", "password": b"irrelevantpassword"}, ValueError),
        # Case 7: Different byte sequences for hashing - making sure password is handled correctly
        (
            {"hash_name": "sha512", "password": b"\xfa\xfb\xfc\xfd\xfe\xff"},
            hashlib.sha512(b"\xfa\xfb\xfc\xfd\xfe\xff").digest(),
        ),
    ],
    "safety": [
        # Case 3: Hash name in hashlib.algorithms_available but not in safe_hash_names
        (
            {"hash_name": "sha1", "password": b"insecurepassword"},
            ValueError,
        ),
        # Case 2: Unsupported hash name
        ({"hash_name": "md5", "password": b"password123"}, ValueError),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = hash_password(**test)
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
            result = hash_password(**test)
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
