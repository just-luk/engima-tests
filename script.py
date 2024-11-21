APPROVED_COMMANDS = ['ls', 'whoami', 'date']

def validate_and_run_cmd(usr_command: str) -> str | None:
    if any(valid_cmd in usr_command for valid_cmd in APPROVED_COMMANDS):
        return usr_command
    return None