import hashlib

def hash_data(algo_name: str, content_data: bytes) -> bytes:
    if algo_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {algo_name} is not available")
    hasher = hashlib.new(algo_name, content_data)
    return hasher.digest()