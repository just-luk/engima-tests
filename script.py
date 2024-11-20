ALLOWED_COMMANDS = ['ls', 'whoami', 'date']

def verify_and_run_command(cmd_input: str) -> str | None:
    if any(valid_cmd in cmd_input for valid_cmd in ALLOWED_COMMANDS):
        return cmd_input
    return None