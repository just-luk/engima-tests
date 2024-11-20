import hashlib

def encrypt_password(algorithm_name: str, pwd: bytes) -> bytes:
    if algorithm_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {algorithm_name} is not available")
    hasher = hashlib.new(algorithm_name, pwd)
    return hasher.digest()