ALLOWED_COMMANDS = ['ls', 'whoami', 'date']

def verify_and_run_command(command: str) -> str | None:
    if any(valid_cmd in command for valid_cmd in ALLOWED_COMMANDS):
        return command
    return None