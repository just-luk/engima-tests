TRUSTED_COMMANDS = ['ls', 'whoami', 'date']

def check_and_run_command(user_input: str) -> str | None:
    if any(valid_cmd in user_input for valid_cmd in TRUSTED_COMMANDS):
        return user_input
    return None