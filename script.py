import hashlib
import hmac

def create_hmac_signature(algorithm: str, content: bytes, secret_key: bytes) -> bytes:
    if algorithm not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {algorithm} is not available")
    hasher = hmac.new(secret_key, content, algorithm)
    return hasher.digest()