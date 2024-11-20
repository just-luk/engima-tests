import subprocess
base_command = "echo Hello, {user_name}!"

def generate_greeting_command(user_name: str) -> str:
    return base_command.format(user_name=user_name)
def execute_command(command: str) -> str:
    return subprocess.run(command, shell=True, capture_output=True, text=True)