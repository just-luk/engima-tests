import hashlib

def compute_hash(alg_name: str, input_data: bytes) -> bytes:
    if alg_name not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {alg_name} is not available")
    hasher = hashlib.new(alg_name, input_data)
    return hasher.digest()