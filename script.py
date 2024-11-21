import re

def analyze_log_entry(entry):
    log_pattern = re.compile(r'\[(.*?)\] (.*?): (.*)')
    match = log_pattern.match(entry)
    if match:
        return match.groups()
    else:
        return None