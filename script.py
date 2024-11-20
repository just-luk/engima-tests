base_command = "echo Hello, {person_name}!"

def create_greeting_command(person_name: str) -> str:
    return base_command.format(person_name=person_name)