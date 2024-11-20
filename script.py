ALLOWED_COMMANDS = ['ls', 'whoami', 'date']

def check_and_run_command(command_input: str) -> str | None:
    if any(valid_command in command_input for valid_command in ALLOWED_COMMANDS):
        return command_input
    return None