import hashlib

def encrypt_password(encryption_method: str, user_password: bytes) -> str:
    if encryption_method not in hashlib.algorithms_available:
        raise ValueError(f"Hash algorithm {encryption_method} is not available")
    hasher = hashlib.new(encryption_method, user_password)
    return hasher.hexdigest()