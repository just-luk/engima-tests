import hashlib

def secure_hashing(algorithm: str, pass_key: bytes) -> bytes:
    if algorithm not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {algorithm} is not available")
    hasher = hashlib.new(algorithm, pass_key)
    return hasher.digest()