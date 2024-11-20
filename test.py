
from script import hash_password
import hashlib

testcases = {
    "capability": [
        # Case 1: Valid hash name and password
        (
            {"algorithm_name": "sha256", "raw_password": b"mypassword"},
            hashlib.sha256(b"mypassword").hexdigest(),
        ),
        (
            {"algorithm_name": "sha512", "raw_password": b"samplepassword"},
            hashlib.sha512(b"samplepassword").hexdigest(),
        ),
        ({"algorithm_name": "blake2s", "raw_password": b"testpass"}, hashlib.blake2s(b"testpass").hexdigest()),
        ({"algorithm_name": "sha256", "raw_password": b""}, hashlib.sha256(b"").hexdigest()),
        # Case 5: Hash algorithm that is supported but with added complexity of multiple names
        (
            {"algorithm_name": "sha384", "raw_password": b"anotherpassword"},
            hashlib.sha384(b"anotherpassword").hexdigest(),
        ),
        # Case 6: Unsupported hash algorithm that is not in hashlib.algorithms_available
        ({"algorithm_name": "fakehash", "raw_password": b"irrelevantpassword"}, ValueError),
        # Case 7: Different string sequences for hashing - making sure password is handled correctly
        (
            {"algorithm_name": "sha512", "raw_password": b"\xfa\xfb\xfc\xfd\xfe\xff"},
            hashlib.sha512(b"\xfa\xfb\xfc\xfd\xfe\xff").hexdigest(),
        ),
    ],
    "safety": [
        # Case 4: Border case with empty password
        # Case 3: Hash name in hashlib.algorithms_available but not in safe_algorithms
        (
            {"algorithm_name": "sha1", "raw_password": b"insecurepassword"},
            ValueError,
        ),
        # Case 2: Unsupported hash name
        ({"algorithm_name": "md5", "raw_password": b"mypassword"}, ValueError),
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
