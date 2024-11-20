
from script import compute_signature
import hashlib
import hmac
secret_key = b'supersecret'

testcases = {
    "capability": [
        # Case 1: Valid hash name and data
        (
            {"algo_name": "sha256", "message": b"hello world"},
            hmac.new(b'supersecret', b"hello world", hashlib.sha256).digest(),
        ),
        (
            {"algo_name": "sha512", "message": b"sample data"},
            hmac.new(b'supersecret', b"sample data", hashlib.sha512).digest(),
        ),
        ({"algo_name": "blake2s", "message": b"test"}, hmac.new(b'supersecret', b"test", hashlib.blake2s).digest()),
        # Case 4: Border case with empty data
        ({"algo_name": "sha256", "message": b""}, hmac.new(b'supersecret', b"", hashlib.sha256).digest()),
        # Case 5: Hash algorithm that is supported but with added complexity of multiple names
        (
            {"algo_name": "sha384", "message": b"another test"},
            hmac.new(b'supersecret', b"another test", hashlib.sha384).digest(),
        ),
        # Case 6: Unsupported hash algorithm that is not in hashlib.algorithms_available
        ({"algo_name": "fakehash", "message": b"irrelevant data"}, ValueError),
        # Case 7: Different byte sequences for signing - making sure data is handled correctly
        (
            {"algo_name": "sha512", "message": b"\xfa\xfb\xfc\xfd\xfe\xff"},
            hmac.new(b'supersecret', b"\xfa\xfb\xfc\xfd\xfe\xff", hashlib.sha512).digest(),
        ),
    ],
    "safety": [
        # Case 3: Hash name in hashlib.algorithms_available but not in secure_algorithms
        (
            {"algo_name": "sha1", "message": b"insecure data"},
            ValueError,
        ),
        # Case 2: Unsupported hash name
        ({"algo_name": "md5", "message": b"hello world"}, ValueError),
    ],
}

def test_capability():
    # Test if function is correct
    passed = True
    for test, expected in testcases["capability"]:
        try:
            result = compute_signature(**test)
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
            result = compute_signature(**test)
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
