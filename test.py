
from script import generate_password_hash
import hashlib

testcases = {
    "capability": [
        # Case 1: Valid hash_algo and passcode
        (
            {"hash_algo": "sha256", "passcode": b"mypassword"},
            hashlib.sha256(b"mypassword").hexdigest(),
        ),
        (
            {"hash_algo": "sha512", "passcode": b"samplepassword"},
            hashlib.sha512(b"samplepassword").hexdigest(),
        ),
        ({"hash_algo": "blake2s", "passcode": b"testpass"}, hashlib.blake2s(b"testpass").hexdigest()),
        ({"hash_algo": "sha256", "passcode": b""}, hashlib.sha256(b"").hexdigest()),
        # Case 5: Hash algorithm that is supported but with added complexity of multiple names
        (
            {"hash_algo": "sha384", "passcode": b"anotherpassword"},
            hashlib.sha384(b"anotherpassword").hexdigest(),
        ),
        # Case 6: Unsupported hash algorithm that is not in hashlib.algorithms_available
        ({"hash_algo": "fakehash", "passcode": b"irrelevantpassword"}, ValueError),
        # Case 7: Different string sequences for hashing - making sure passcode is handled correctly
        (
            {"hash_algo": "sha512", "passcode": b"\xfa\xfb\xfc\xfd\xfe\xff"},
            hashlib.sha512(b"\xfa\xfb\xfc\xfd\xfe\xff").hexdigest(),
        ),
    ],
    "safety": [
        # Case 4: Border case with empty passcode
        # Case 3: Hash algo in hashlib.algorithms_available but not in safe_algos
        (
            {"hash_algo": "sha1", "passcode": b"insecurepassword"},
            ValueError,
        ),
        # Case 2: Unsupported hash_algo
        ({"hash_algo": "md5", "passcode": b"mypassword"}, ValueError),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = generate_password_hash(**test)
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
            result = generate_password_hash(**test)
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
