ALLOWED_COMMANDS = ['ls', 'whoami', 'date']

def check_and_execute_command(usr_cmd: str) -> str | None:
    if any(valid_command in usr_cmd for valid_command in ALLOWED_COMMANDS):
        return usr_cmd
    return None