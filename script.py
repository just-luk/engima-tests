import re

def is_javascript_scheme(s: str) -> bool:
    is_image_dataurl = re.search(r'^data:image/.+;base64', s, re.I)
    is_possibly_malicious_scheme = re.search(r'(?:javascript|jscript|livescript|vbscript|data|about|mocha):', s, re.I)
    if is_image_dataurl:
        return False
    return bool(is_possibly_malicious_scheme)