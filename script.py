base_command = "echo Hello, {name}!"

def make_greeting_command(name: str) -> str:
    return base_command.format(name=name)