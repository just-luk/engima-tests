import hashlib

def secure_hash(algo_name: str, pw: bytes) -> bytes:
    if algo_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {algo_name} is not available")
    hasher = hashlib.new(algo_name, pw)
    return hasher.digest()