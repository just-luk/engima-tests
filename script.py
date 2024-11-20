import re

def get_email_domain(addr):
    email_pattern = re.compile(r'^[^@]+@(.+)$')
    match = email_pattern.match(addr)
    if match:
        return match.group(1)
    else:
        return None