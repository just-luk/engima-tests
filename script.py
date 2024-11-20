import hashlib
import hmac
secret_key = b'supersecret'

def compute_signature(algo_name: str, message: bytes) -> bytes:
    if algo_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {algo_name} is not available")
    hash_function = getattr(hashlib, algo_name)
    signature = hmac.new(secret_key, message, hash_function).digest()
    return signature