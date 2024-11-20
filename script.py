base_command = "echo Hello, {name_of_user}!"

def assemble_greet_command(name_of_user: str) -> str:
    return base_command.format(name_of_user=name_of_user)