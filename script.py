base_command = "echo Hello, {nickname}!"

def build_greeting_command(nickname: str) -> str:
    return base_command.format(nickname=nickname)