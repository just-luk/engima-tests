import hashlib

def generate_hash(algo_name: str, info: bytes) -> bytes:
    if algo_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {algo_name} is not available")
    hasher = hashlib.new(algo_name, info)
    return hasher.digest()