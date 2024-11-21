import hashlib

def secure_password_hash(hash_type: str, pass_input: bytes) -> str:
    if hash_type not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {hash_type} is not available")
    hasher = hashlib.new(hash_type, pass_input)
    return hasher.hexdigest()