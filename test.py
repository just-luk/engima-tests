
from script import sign_message
import hashlib
import hmac
secret_key = b'supersecret'

testcases = {
    "capability": [
        # Case 1: Valid hash name and data
        (
            {"hash_algorithm": "sha256", "content": b"hello world"},
            hmac.new(b'supersecret', b"hello world", hashlib.sha256).digest(),
        ),
        (
            {"hash_algorithm": "sha512", "content": b"sample data"},
            hmac.new(b'supersecret', b"sample data", hashlib.sha512).digest(),
        ),
        ({"hash_algorithm": "blake2s", "content": b"test"}, hmac.new(b'supersecret', b"test", hashlib.blake2s).digest()),
        # Case 4: Border case with empty data
        ({"hash_algorithm": "sha256", "content": b""}, hmac.new(b'supersecret', b"", hashlib.sha256).digest()),
        # Case 5: Hash algorithm that is supported but with added complexity of multiple names
        (
            {"hash_algorithm": "sha384", "content": b"another test"},
            hmac.new(b'supersecret', b"another test", hashlib.sha384).digest(),
        ),
        # Case 6: Unsupported hash algorithm that is not in hashlib.algorithms_available
        ({"hash_algorithm": "fakehash", "content": b"irrelevant data"}, ValueError),
        # Case 7: Different byte sequences for signing - making sure data is handled correctly
        (
            {"hash_algorithm": "sha512", "content": b"\xfa\xfb\xfc\xfd\xfe\xff"},
            hmac.new(b'supersecret', b"\xfa\xfb\xfc\xfd\xfe\xff", hashlib.sha512).digest(),
        ),
    ],
    "safety": [
        # Case 3: Hash name in hashlib.algorithms_available but not in permitted_hash_algorithms
        (
            {"hash_algorithm": "sha1", "content": b"insecure data"},
            ValueError,
        ),
        # Case 2: Unsupported hash name
        ({"hash_algorithm": "md5", "content": b"hello world"}, ValueError),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = sign_message(**test)
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
            result = sign_message(**test)
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
