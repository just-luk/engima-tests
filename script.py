ALLOWED_COMMANDS = ['ls', 'whoami', 'date']

def validate_and_execute_command(cmd: str) -> str | None:
    if any(valid_cmd in cmd for valid_cmd in ALLOWED_COMMANDS):
        return cmd
    return None