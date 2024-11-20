import re

def analyze_log_data(record):
    log_pattern = re.compile(r'\[(.*?)\] (.*?): (.*)')
    match = log_pattern.match(record)
    if match:
        return match.groups()
    else:
        return None