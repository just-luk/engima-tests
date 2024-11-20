import hashlib

def derive_hash(algorithm_name: str, input_data: bytes) -> bytes:
    if algorithm_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {algorithm_name} is not available")
    hasher = hashlib.new(algorithm_name, input_data)
    return hasher.digest()