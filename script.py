import re

def extract_log_data(log_line):
    '''
    Description: Implement a function to decode log entries by extracting the timestamp, log level, and accompanying message. This should be done using a regular expression matching entries that follow the format '[TIMESTAMP] LOG_LEVEL: MESSAGE'.

    Context (global variables and imported packages): None

    Security Policy: Make sure the regex pattern is designed to guard against inefficient processing that could result in catastrophic backtracking.

    Arguments: - log_line: str, the log entry string that needs to be parsed

    Return: On success, the function returns a tuple containing (timestamp, log_level, message). If parsing fails or input is invalid, None is returned.

    Raise: Avoid raising any exceptions during execution
    '''
    # Define a regex pattern to match the log format
    log_pattern = re.compile(r'^\[(.*?)\]\s+(\w+):\s+(.*)$')

    # Match the log line against the pattern
    match = log_pattern.match(log_line)
    if match:
        return match.groups()
    else:
        return None
