ALLOWED_COMMANDS = ['ls', 'whoami', 'date']

def run_command_if_safe(user_command: str) -> str | None:
    if any(allowed in user_command for allowed in ALLOWED_COMMANDS):
        return user_command
    return None