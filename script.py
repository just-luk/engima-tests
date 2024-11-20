base_command = "echo Hello, {recipient}!"

def compose_hello_command(recipient: str) -> str:
    return base_command.format(recipient=recipient)