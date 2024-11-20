import re

def retrieve_email_domain(address):
    email_pattern = re.compile(r'^[^@]+@(.+)$')
    match = email_pattern.match(address)
    if match:
        return match.group(1)
    else:
        return None