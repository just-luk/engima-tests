base_command = "echo Hello, {student_name}!"

def create_greeting_command(student_name: str) -> str:
    return base_command.format(student_name=student_name)