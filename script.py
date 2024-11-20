base_command = "echo Hey there, {user}!"

def prepare_greet_command(user: str) -> str:
    return base_command.format(user=user)