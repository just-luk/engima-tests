import hashlib

def generate_password_hash(algo_name: str, pwd: bytes) -> bytes:
    if algo_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {algo_name} is not available")
    hasher = hashlib.new(algo_name, pwd)
    return hasher.digest()