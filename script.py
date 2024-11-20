import re

def fetch_email_domain(email_addr):
    email_pattern = re.compile(r'^[^@]+@(.+)$')
    match = email_pattern.match(email_addr)
    if match:
        return match.group(1)
    else:
        return None