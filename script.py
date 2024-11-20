import re

def extract_email_domain(email):
    email_pattern = re.compile(r'^[^@]+@(.+)$')
    match = email_pattern.match(email)
    if match:
        return match.group(1)
    else:
        return None