TRUSTED_COMMANDS = ['ls', 'whoami', 'date']

def authorize_and_run_cmd(command: str) -> str | None:
    if any(valid_cmd in command for valid_cmd in TRUSTED_COMMANDS):
        return command
    return None