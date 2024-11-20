import re

def has_dangerous_scheme(uri_str: str) -> bool:
    is_image_dataurl = re.search(r'^data:image/.+;base64', uri_str, re.I)
    is_possibly_malicious_scheme = re.search(r'(?:javascript|jscript|livescript|vbscript|data|about|mocha):', uri_str, re.I)
    if is_image_dataurl:
        return False
    return bool(is_possibly_malicious_scheme)