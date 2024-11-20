import hashlib
import hmac
secret_key = b'supersecret'

def sign_data(algorithm: str, message: bytes) -> bytes:
    if algorithm not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {algorithm} is not available")
    hash_function = getattr(hashlib, algorithm)
    signature = hmac.new(secret_key, message, hash_function).digest()
    return signature