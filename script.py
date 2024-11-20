base_command = "echo Hello, {username}!"

def create_greeting_command(username: str) -> str:
    return base_command.format(username=username)