import hashlib

def compute_digest(algorithm_name: str, content: bytes) -> bytes:
    if algorithm_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {algorithm_name} is not available")
    hasher = hashlib.new(algorithm_name, content)
    return hasher.digest()