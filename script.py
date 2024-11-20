base_command = "echo Welcome, {user_fullname}!"

def build_greeting_script(user_fullname: str) -> str:
    return base_command.format(user_fullname=user_fullname)